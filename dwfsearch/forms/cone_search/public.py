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

    ra = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '1'}
        ),
        label=_('RA (degrees)'),
        required=True,
    )

    dec = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '2'}
        ),
        label=_('DEC (degrees)'),
        required=True,
    )

    radius = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'tabindex': '3'}
        ),
        label=_('Search Radius (arcsecond)'),
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
        ra = self.cleaned_data.get('ra')

        if not 0 <= ra <= 360:
            raise ValidationError(_('RA out of range [0, +360]'))

    def clean_dec(self):
        dec = self.cleaned_data.get('dec')

        if not -90 <= dec <= 90:
            raise ValidationError(_('DEC out of range [-90, +90]'))

    def clean_radius(self):
        radius = self.cleaned_data.get('radius')

        if not 0 <= radius:
            raise ValidationError(_('Radius must be non-negative'))

    def get_search_query(self):
        query_parts = dict()
        for field in self.fields:
            query_parts.update({
                field: self.data.get(field),
            })
        return query_parts
