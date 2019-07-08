"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from ...models import JobParameter
from ...utility.utils import utc_current_yymmdd_date

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
    'image_names'
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
    'image_names': _('6 digit code in the NOAO name'),
}


class JobParameterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.job = kwargs.pop('job', None)
        super(JobParameterForm, self).__init__(*args, **kwargs)
        self.fields['field'].widget.attrs.update({'class': 'form-control'})
        # setting up the UTC date as current date.
        self.fields['date'].initial = utc_current_yymmdd_date()
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
        self.fields['image_names'].widget.attrs.update({'class': 'form-control'})

    class Meta(object):
        model = JobParameter
        fields = FIELDS
        labels = LABELS

    def update_fields_to_required(self):
        for field_name in self.fields:
            self.fields[field_name].required = True

    def get_data(self, parameter_name):
        data = self.cleaned_data

        return data.get(parameter_name, None)

    def save(self, **kwargs):
        """
        Overrides the default save method
        :param kwargs: Dictionary of keyword arguments
        :return: instance of the model
        """
        self.full_clean()
        # data = self.cleaned_data

        # create default data dictionary
        data_dict = {}
        for field_name in self.fields:
            data_dict.update({
                field_name: self.get_data(field_name)
            })

        job_parameter, created = JobParameter.objects.update_or_create(
            job=self.job,
            defaults=data_dict,
        )

        return job_parameter
