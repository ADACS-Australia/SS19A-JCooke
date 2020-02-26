"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ..models import (
    UserRoleRequest,
    UserRole,
)


APPROVE = 'Approve'
REJECT = 'Reject'
DELETE = 'Delete'

action_options = (
    (UserRoleRequest.APPROVED, APPROVE),
    (UserRoleRequest.REJECTED, REJECT),
    (UserRoleRequest.DELETED, DELETE),
)


class RoleChangeRequestActionForm(forms.Form):
    """
    Model form to Action on a Request to Change Role
    """

    action = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'tabindex': '1'}
        ),
        choices=action_options,
    )

    response = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'tabindex': '2'}
        ),
        label=_('Response Text'),
        required=False,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': "form-control", 'tabindex': '3'},
        ),
        label=_('Your Password'),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RoleChangeRequestActionForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not self.user.check_password(password):
            raise ValidationError('Incorrect Password')

    def save(self, instance, *args, **kwargs):
        data = self.cleaned_data
        instance.actioned_by = self.user
        instance.action_time = timezone.now()
        instance.response = data['response']
        try:
            instance.status = int(data['action'])
        except (ValueError, TypeError):
            raise ValidationError('Invalid status code')
        instance.save()

        if int(data['action']) in [UserRoleRequest.APPROVED, ]:
            UserRole.objects.update_or_create(
                user=instance.user,
                defaults={
                    'role': instance.intended_role,
                }
            )
