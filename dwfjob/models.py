"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from django_hpc_job_controller.models import HpcJob

from dwfcommon.utility.display_names import *

from .validators import (
    validate_yymmdd_date,
    validate_cs_yymmdd_dates,
)


class MaryJob(HpcJob):
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
    job = models.ForeignKey(MaryJob, on_delete=models.CASCADE, blank=False, null=False)

    field = models.CharField(max_length=255, blank=False, null=False)

    date = models.CharField(max_length=6, blank=False, null=False, validators=[validate_yymmdd_date, ])

    MAKE_TEMPLATE = 'make_template'
    MAKE_TEMPLATE_DISPLAY = 'Make Template'
    OLD_TEMPLATE = 'old_template'
    OLD_TEMPLATE_DISPLAY = 'Old Template'
    NEW_TEMPLATE = 'new_template'
    NEW_TEMPLATE_DISPLAY = 'New Template'

    TEMPLATE_CHOICES = [
        (MAKE_TEMPLATE, MAKE_TEMPLATE_DISPLAY),
        (OLD_TEMPLATE, OLD_TEMPLATE_DISPLAY),
        (NEW_TEMPLATE, NEW_TEMPLATE_DISPLAY),
    ]

    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, blank=False, null=False, default=NEW_TEMPLATE)

    template_date = models.CharField(max_length=6, blank=True, null=True, validators=[validate_yymmdd_date, ])

    RT = 'rt'
    NOAO = 'NOAO'
    LT = 'lt'

    MARY_SEED_NAME_CHOICES = [
        (RT, RT),
        (NOAO, NOAO),
        (LT, LT),
    ]

    mary_seed_name = models.CharField(max_length=20, choices=MARY_SEED_NAME_CHOICES, blank=False, null=False,
                                      default=RT)
    steps = models.SmallIntegerField(choices=list(zip(range(1, 301), range(1, 301))), blank=False, null=False,
                                     default=1)

    TRUE = 'True'
    FALSE = 'False'

    CLOBBER_CHOICES = [
        (FALSE, FALSE),
        (TRUE, TRUE),
    ]

    clobber = models.CharField(max_length=20, choices=CLOBBER_CHOICES, blank=False, null=False, default=FALSE)

    U_BAND = 'u Band'
    U_BAND_VALUE = 'u'
    G_BAND = 'g Band'
    G_BAND_VALUE = 'g'
    R_BAND = 'r Band'
    R_BAND_VALUE = 'r'
    I_BAND = 'i Band'
    I_BAND_VALUE = 'i'
    Z_BAND = 'z Band'
    Z_BAND_VALUE = 'z'
    Y_BAND = 'Y Band'
    Y_BAND_VALUE = 'Y'

    FILTER_CHOICES = [
        (U_BAND_VALUE, U_BAND),
        (G_BAND_VALUE, G_BAND),
        (R_BAND_VALUE, R_BAND),
        (I_BAND_VALUE, I_BAND),
        (Z_BAND_VALUE, Z_BAND),
        (Y_BAND_VALUE, Y_BAND),
    ]

    filter = models.CharField(max_length=20, choices=FILTER_CHOICES, blank=False, null=False, default=G_BAND)

    old_template_name = models.CharField(max_length=2048, blank=True, null=True)

    mary_run_template = models.CharField(max_length=6, blank=True, null=True, validators=[validate_yymmdd_date, ])

    mary_run_template_sequence_number = models.CharField(max_length=255, blank=True, null=True)

    image_names = models.CharField(max_length=2048, blank=False, null=False, validators=[
        RegexValidator(
            regex='^(\d{6}|\d{7})(\s*,\s*(\d{6}|\d{7}))*$',
            message='Must be comma separated 6/7 digit codes',
            code='invalid_image_names',
        )
    ])

    run_dates = models.CharField(max_length=2048, blank=False, null=False, validators=[validate_cs_yymmdd_dates, ])

    template_images = models.CharField(max_length=2048, blank=True, null=True, validators=[
        RegexValidator(
            regex='^[0-9]{6}(\s*,\s*[0-9]{6})*$',
            message='Must be comma separated 6 digit codes',
            code='invalid_template_images',
        )
    ])

    last_mary_run = models.IntegerField(blank=False, null=False)
