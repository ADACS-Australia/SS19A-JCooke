"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from ...models import JobParameter


FIELDS = ['field', 'date', 'template', 'template_date', 'mary_seed_name', 'steps', 'clobber', 'filter',
          'old_template_name', 'mary_run_template', 'mary_run_template_sequence_number']


class MaryJobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MaryJobForm, self).__init__(*args, **kwargs)

    class Meta(object):
        model = JobParameter
        fields = FIELDS
