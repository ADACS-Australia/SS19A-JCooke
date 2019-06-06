"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.conf import settings
from django.db import models

from django_hpc_job_controller.models import HpcJob

from .utility.display_names import *


class Job(HpcJob):
    """
    Job model extending HpcJob
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        (NONE, NONE_DISPLAY),
        (PUBLIC, PUBLIC_DISPLAY),
    ]

    extra_status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, default=NONE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    json_representation = models.TextField(null=True, blank=True)

    @property
    def status_display(self):
        """
        Finds and return the corresponding status display for a status
        :return: String of status display
        """
        if self.extra_status != NONE:
            return DISPLAY_NAME_MAP[self.extra_status]
        if self.job_status in DISPLAY_NAME_MAP_HPC_JOB:
            return DISPLAY_NAME_MAP[DISPLAY_NAME_MAP_HPC_JOB[self.job_status]]
        return "Unknown"

    @property
    def status(self):
        """
        Finds and return the corresponding status for a status number
        :return: String of status
        """
        if self.extra_status != NONE:
            return self.extra_status
        if self.job_status in DISPLAY_NAME_MAP_HPC_JOB:
            return DISPLAY_NAME_MAP_HPC_JOB[self.job_status]
        return "unknown"

    class Meta:
        unique_together = (
            ('user', 'name'),
        )

    def __str__(self):
        return '{}'.format(self.name)

    def as_json(self):
        return dict(
            id=self.id,
            value=dict(
                name=self.name,
                username=self.user.username,
                status=self.status,
                creation_time=self.creation_time.strftime('%d %b %Y %I:%m %p'),
            ),
        )


class JobParameter(models.Model):
    field = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)

    OLD_TEMPLATE = 'Old Template'
    NEW_TEMPLATE = 'New Template'

    TEMPLATE_CHOICES = [
        (OLD_TEMPLATE, OLD_TEMPLATE),
        (NEW_TEMPLATE, NEW_TEMPLATE),
    ]

    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, blank=False, null=False, default=NEW_TEMPLATE)
    template_date = models.DateField(blank=True, null=True)

    RT = 'rt'
    NOAO = 'NOAO'

    MARY_SEED_NAME_CHOICES = [
        (RT, RT),
        (NOAO, NOAO),
    ]

    mary_seed_name = models.CharField(max_length=20, choices=MARY_SEED_NAME_CHOICES, blank=False, null=False,
                                      default=RT)
