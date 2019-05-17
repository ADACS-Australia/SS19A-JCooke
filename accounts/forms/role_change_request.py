"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import UserRoleRequest


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
    def __init__(self, *args, **kwargs):
        super(RoleChangeRequestForm, self).__init__(*args, **kwargs)
        self.fields['intended_role'].required = True

    class Meta:
        model = UserRoleRequest
        fields = FIELDS
        labels = LABELS
        widgets = WIDGETS
