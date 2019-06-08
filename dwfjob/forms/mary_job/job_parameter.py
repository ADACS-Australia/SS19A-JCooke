"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
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


class JobParameterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(JobParameterForm, self).__init__(*args, **kwargs)
        self.fields['field'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['template'].widget.attrs.update({'class': 'form-control'})
        self.fields['template_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['mary_seed_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['steps'].widget.attrs.update({'class': 'form-control'})
        self.fields['clobber'].widget.attrs.update({'class': 'form-control'})
        self.fields['filter'].widget.attrs.update({'class': 'form-control'})
        self.fields['old_template_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['mary_run_template'].widget.attrs.update({'class': 'form-control'})
        self.fields['mary_run_template_sequence_number'].widget.attrs.update({'class': 'form-control'})

    class Meta(object):
        model = JobParameter
        fields = FIELDS
        labels = LABELS
