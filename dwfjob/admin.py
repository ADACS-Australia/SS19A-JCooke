"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib import admin

from .models import (
    MaryJob,
    JobParameter,
)


@admin.register(MaryJob)
class MaryJob(admin.ModelAdmin):
    list_display = ('user', 'name', 'status',)
    search_fields = ['user', 'name', 'status', ]


@admin.register(JobParameter)
class JobParameter(admin.ModelAdmin):
    list_display = (
        'job',
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
        'image_names',
        'run_dates',
        'template_images',
    )
    search_fields = ['job__name', 'date']
