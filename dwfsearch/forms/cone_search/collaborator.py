"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .public import ConeSearchForm


class ConeSearchCollaboratorForm(ConeSearchForm):
    """
    Form to performing cone search
    """

    mary_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '5'}
        ),
        label=_('MaryRun ID'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ConeSearchCollaboratorForm, self).__init__(*args, **kwargs)

    def clean_mary_id(self):
        mary_id = self.cleaned_data.get('mary_id')

        if mary_id and mary_id < 0:
            raise ValidationError(_('Invalid MaryRun ID'))

