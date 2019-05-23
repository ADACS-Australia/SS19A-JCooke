"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import reverse

from . import templates, email
from ..utility import get_admins


def email_verify_request(to_addresses, first_name, last_name, link):
    """
    Sends out the email address verification email
    :param to_addresses: A list of addresses, in this case the user
    :param first_name: String
    :param last_name: String
    :param link: String containing the url to verify email address
    :return: Nothing
    """

    # setting up the context
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'link': link,
    }

    # Building and sending emails
    email.Email(
        subject=templates.VERIFY_EMAIL_ADDRESS['subject'],
        to_addresses=to_addresses,
        template=templates.VERIFY_EMAIL_ADDRESS['message'],
        context=context,
    ).send_email()


def email_role_change_request_to_admins(user_role_request):
    """
    Sends out email to the admins (core members in this case) notifying the request to role change
    :param user_role_request: UserRoleRequest model instance
    """

    # setting up the context
    context = {
        'first_name': user_role_request.user.first_name,
        'last_name': user_role_request.user.last_name,
        'username': user_role_request.user.username,
        'email': user_role_request.user.email,
        'current_role': user_role_request.current_role.name,
        'intended_role': user_role_request.intended_role.name,
        'link': 'link_to_set',
    }

    email.Email(
        subject=templates.ROLE_CHANGE_REQUEST['subject'],
        to_addresses=get_admins().values_list('email', flat=True),
        template=templates.ROLE_CHANGE_REQUEST['message'],
        context=context,
    ).send_email()
