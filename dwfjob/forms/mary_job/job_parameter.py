"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from ...models import JobParameter

FIELDS = [
    'field',
    'date',
    'template',
    'template_date',
    'mary_seed_name',
    'steps',
    'clobber',
    'filter',
    'old_template_name',
    'mary_run_template',
    'mary_run_template_sequence_number',
]

LABELS = {
    'field': _('Field'),
    'date': _('Date'),
    'template': _('Use template'),
    'template_date': _('Template date'),
    'mary_seed_name': _('Mary run seed name'),
    'steps': _('Number of images to be coadded'),
    'clobber': _('Clobber run'),
    'filter': _('Filter'),
    'old_template_name': _('Name of old template (downloaded from NOAO portal)'),
    'mary_run_template': _('Date of mary template'),
    'mary_run_template_sequence_number': _('Sequence number of previous mary run'),
}

WIDGETS = {
    'date': forms.DateInput(
        format='%d/%m/%Y',
        attrs={
            'class': 'form-control date-picker',
        },
    ),
    'template_date': forms.DateInput(
        format='%d/%m/%Y',
        attrs={
            'class': 'form-control date-picker',
        },
    ),
    'mary_run_template': forms.DateInput(
        format='%d/%m/%Y',
        attrs={
            'class': 'form-control date-picker',
        },
    )
}


class JobParameterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(JobParameterForm, self).__init__(*args, **kwargs)
        self.fields['field'].widget.attrs.update({'class': 'form-control'})
        # setting up the UTC date as current date.
        self.fields['date'].initial = timezone.now()
        self.fields['date'].input_formats = ['%d/%m/%Y', ]
        self.fields['template'].widget.attrs.update({'class': 'form-control'})
        self.fields['template_date'].input_formats = ['%d/%m/%Y', ]
        self.fields['mary_seed_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['steps'].widget.attrs.update({'class': 'form-control'})
        self.fields['clobber'].widget.attrs.update({'class': 'form-control'})
        self.fields['filter'].widget.attrs.update({'class': 'form-control'})
        self.fields['old_template_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['mary_run_template'].input_formats = ['%d/%m/%Y', ]
        self.fields['mary_run_template_sequence_number'].widget.attrs.update({'class': 'form-control'})

    def update_fields_to_required(self):
        for field_name in self.fields:
            self.fields[field_name].required = True

    class Meta(object):
        model = JobParameter
        fields = FIELDS
        labels = LABELS
        widgets = WIDGETS
