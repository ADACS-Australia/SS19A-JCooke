"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class ConeSearchForm(forms.Form):
    """
    Form to performing cone search
    """

    ra = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'tabindex': '1'}
        ),
        label=_('RA (H:M:S)'),
        required=True,
    )

    dec = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '2'}
        ),
        label=_('DEC'),
        required=True,
    )

    radius = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '3'}
        ),
        label=_('Search Radius'),
        required=True,
    )

    target_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'tabindex': '4'}
        ),
        label=_('DWF target name'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ConeSearchForm, self).__init__(*args, **kwargs)

    def clean_ra(self):
        ra = self.cleaned_data.get('ra').split(':')

        try:
            if not 0 <= int(ra[0]) <= 23 or not 0 <= int(ra[1]) <= 59 or not 0 <= int(ra[2]) <= 59:
                raise ValidationError(_('RA out of range [0:0:0, 23:59:59]'))
        except (ValueError, TypeError):
            raise ValidationError(_('RA invalid'))

    def clean_dec(self):
        dec = self.cleaned_data.get('dec')

        if not -90 <= dec <= 90:
            raise ValidationError(_('DEC out of range [-90, +90]'))

    def get_search_query(self):
        query_parts = dict()
        for field in self.fields:
            query_parts.update({
                field: self.data.get(field),
            })
        return query_parts
