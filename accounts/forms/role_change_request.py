"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from ..models import UserRoleRequest, Role, User

FIELDS = ['current_role', 'intended_role', ]

WIDGETS = {
    'current_role': forms.Select(
        attrs={'class': "form-control", 'tabindex': '1'},
    ),
    'intended_role': forms.Select(
        attrs={'class': "form-control", 'tabindex': '2'},
    ),
}

LABELS = {
    'current_role': _('Current Role'),
    'intended_role': _('Intended Role'),
}


class RoleChangeRequestForm(forms.ModelForm):
    """
    Model form to Request to Change Role
    """

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': "form-control", 'tabindex': '3'},
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RoleChangeRequestForm, self).__init__(*args, **kwargs)
        self.fields['intended_role'].queryset = Role.objects.filter(~Q(name=self.user.user_role))
        self.fields['intended_role'].empty_label = None
        self.fields['current_role'].queryset = Role.objects.filter(Q(name=self.user.user_role))
        self.fields['current_role'].empty_label = None

    class Meta:
        model = UserRoleRequest
        fields = FIELDS
        labels = LABELS
        widgets = WIDGETS

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not self.user.check_password(password):
            raise ValidationError('Incorrect Password')

    def save(self, commit=True):

        # setting up the user to the UserRoleRequest form.
        self.instance = UserRoleRequest(
            user=User.objects.get(username=self.user.username),
            current_role=Role.objects.get(pk=self.data['current_role']),
            intended_role=Role.objects.get(pk=self.data['intended_role']),
        )

        super(RoleChangeRequestForm, self).save(commit=commit)
