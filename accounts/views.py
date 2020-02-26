"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from six.moves.urllib import parse

from . import utility
from .constants import ROLE_CHANGE_REQUESTS_PER_PAGE
from .decorators import admin_or_system_admin_required
from .forms.profile import EditProfileForm
from .forms.registation import RegistrationForm
from .forms.verify_email import VerifyForm
from .forms.role_change_request import RoleChangeRequestForm
from .forms.role_change_request_action import RoleChangeRequestActionForm
from .models import (
    User,
    UserRoleRequest,
)

from .mailer import actions


logger = logging.getLogger(__name__)


def registration(request):
    """
    View to process the registration
    :param request: A Django request object
    :return: A rendered HTML template
    """

    # returning to profile if the user is authenticated
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    data = {}
    if request.method == 'POST':

        # creating the registration form from the data
        form = RegistrationForm(request.POST)

        # if form is valid save the information
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            # generating verification link
            verification_link = \
                utility.get_absolute_site_url(request.scheme, request.get_host()) + reverse('verify_account') + \
                '?code=' + \
                utility.get_token(
                    information='type=user&username={}'.format(data.get('username')),
                    validity=utility.get_email_verification_expiry(),
                )

            # Sending email to the potential user to verify the email address
            actions.email_verify_request(
                to_addresses=[data.get('email')],
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                link=verification_link,
            )

            return render(
                request,
                "accounts/notification.html",
                {
                    'type': 'registration_submitted',
                    'data': data,
                },
            )
    else:

        # get request will serve a blank form
        form = RegistrationForm()

    return render(
        request,
        "accounts/registration.html",
        {
            'form': form,
            'data': data,
            'submit_text': 'Register',
        },
    )


@login_required
def profile(request):
    """
    View to process the profile updates
    :param request: A Django request object
    :return: A rendered HTML template
    """

    data = {}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Information successfully updated', 'alert alert-success')
            return render(
                request,
                "accounts/profile.html",
                {
                    'form': form,
                    'type': 'update_profile_success',
                    'data': data,
                },
            )
        else:
            messages.error(request, 'Please correct the error(s) below.', 'alert alert-warning')
    else:
        form = EditProfileForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            'form': form,
            'data': data,
            'submit_text': 'Update',
        },
    )


@login_required
def request_change_role(request):
    """
    View to request change of role
    :param request:
    :return:
    """

    data = {}
    if request.method == 'POST':
        form = RoleChangeRequestForm(request.POST, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Information successfully recorded', 'alert alert-success')
            return render(
                request,
                "accounts/role_change/role_change.html",
                {
                    'form': form,
                    'type': 'update_profile_success',
                    'data': data,
                },
            )
        else:
            messages.error(request, 'Please correct the error(s) below.', 'alert alert-warning')
    else:
        form = RoleChangeRequestForm(user=request.user)

    return render(
        request,
        "accounts/role_change/role_change.html",
        {
            'form': form,
            'data': data,
            'submit_text': 'Submit Request',
        },
    )


@login_required
@admin_or_system_admin_required
def view_change_role_requests(request):
    user_role_requests_all = UserRoleRequest.objects.filter(~Q(status__in=[UserRoleRequest.DELETED])).order_by('status')

    paginator = Paginator(user_role_requests_all, ROLE_CHANGE_REQUESTS_PER_PAGE)

    page = request.GET.get('page')
    user_role_requests = paginator.get_page(page)

    return render(
        request,
        "accounts/role_change/view_role_change_requests.html",
        {
            'user_role_requests': user_role_requests,
        },
    )


@login_required
@admin_or_system_admin_required
def view_change_role_request(request, request_id=None):
    try:
        user_role_request = UserRoleRequest.objects.get(id=request_id)
    except UserRoleRequest.DoesNotExist:
        raise Http404
    else:
        if user_role_request.status == user_role_request.DELETED:
            raise Http404

    if request.method == 'POST':
        form = RoleChangeRequestActionForm(request.POST, user=request.user)
        if form.is_valid():
            form.save(instance=user_role_request)
        else:
            messages.error(request, 'Please correct the error(s) below.', 'alert alert-warning')
    else:
        form = RoleChangeRequestActionForm(user=request.user)

    return render(
        request,
        "accounts/role_change/role_change_request_action.html",
        {
            'form': form,
            'user_role_request': user_role_request,
        },
    )


def verify(request):
    """
    View to verify a request, using verification table
    :param request:
    :return:
    """
    data = {}

    if request.method == 'POST':
        verify_email_form = VerifyForm(request.POST)

        if verify_email_form.is_valid():
            try:
                # decrypt the code and its parts
                code = utility.get_information(token=verify_email_form.cleaned_data.get('code', ''), reuse=False)
                params = dict(parse.parse_qsl(code))
                verify_type = params.get('type', None)

                # if the verification is for user email address
                if verify_type == 'user':

                    # finds username from the retrieved information
                    username = params.get('username', None)

                    # get the user
                    try:
                        user = User.objects.get(username=username)

                        user.status = user.VERIFIED
                        user.is_active = True
                        user.save()

                        data.update(
                            success=True,
                            message='The email address has been verified successfully',
                        )

                    except User.DoesNotExist:
                        data.update(
                            success=False,
                            message='The requested user account to verify does not exist',
                        )
            except ValueError as e:
                data.update(
                    success=False,
                    message=e if e else 'Invalid verification code',
                )

        else:
            data.update(
                success=False,
                message='Invalid Verification Code/Captcha Failed',
            )
    else:

        code_encrypted = request.GET.get('code', None)

        if code_encrypted:
            try:
                # decrypt the code and its parts
                code = utility.get_information(token=code_encrypted, reuse=True)
                params = dict(parse.parse_qsl(code))
                verify_type = params.get('type', None)

                # if the verification is for user email address
                if verify_type == 'user':

                    # finds username from the retrieved information
                    username = params.get('username', None)

                    # get the user
                    try:
                        user = User.objects.get(
                            username=username,
                            is_active=False,
                            status=User.UNVERIFIED,
                        )

                        data.update({
                            'username': user.username,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'email': user.email,
                        })

                        verify_email_form = VerifyForm()

                        verify_email_form.fields['code'].initial = code_encrypted

                        return render(
                            request,
                            "accounts/verify_email.html",
                            {
                                'form': verify_email_form,
                                'submit_text': 'Proceed',
                                'data': data,
                            },
                        )

                    except User.DoesNotExist:
                        data.update(
                            success=False,
                            message='The requested user account to verify does not exist',
                        )

            except ValueError as e:
                data.update(
                    success=False,
                    message=e if e else 'Invalid verification code',
                )
        else:
            data.update(
                success=False,
                message='Invalid Verification Code',
            )

    return render(
        request,
        "accounts/notification.html",
        {
            'type': 'email_verify',
            'data': data,
        },
    )
