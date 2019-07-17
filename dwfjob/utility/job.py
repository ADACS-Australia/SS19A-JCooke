"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import json
from collections import OrderedDict

from django.core.serializers.json import DjangoJSONEncoder

from dwfcommon.utility.utils import (
    list_job_actions,
    generate_draft_job_name,
    get_formatted_value_for_json,
)

from ..models import (
    MaryJob,
    JobParameter,
)


def clone_job_data(from_job, to_job):
    """
    Copy job data across two jobs
    :param from_job: instance of MaryJob that will be used as a source
    :param to_job: instance of MaryJob that will be used as a target
    :return: Nothing
    """
    # cloning data and data parameters
    try:
        from_job_parameter = JobParameter.objects.get(job=from_job)
        JobParameter.objects.create(
            job=to_job,
            field=from_job_parameter.field,
            date=from_job_parameter.date,
            template=from_job_parameter.template,
            template_date=from_job_parameter.template_date,
            mary_seed_name=from_job_parameter.mary_seed_name,
            steps=from_job_parameter.steps,
            clobber=from_job_parameter.clobber,
            filter=from_job_parameter.filter,
            old_template_name=from_job_parameter.old_template_name,
            mary_run_template=from_job_parameter.mary_run_template,
            mary_run_template_sequence_number=from_job_parameter.mary_run_template_sequence_number,
            image_names=from_job_parameter.image_names,
        )
    except JobParameter.DoesNotExist:
        pass


class DwfMaryJob(object):
    """
    Class representing a MaryJob. The dwf job parameters are scattered in different models in the database.
    This class used to collects the correct job parameters in one place. It also defines the json representation
    of the job.
    """

    # variable to hold the MaryJob model instance
    job = None

    # list to hold the Job Parameter
    job_parameter = None

    # dictionary to hold the filtered Job Parameters according to the template choice
    job_parameters = None

    # what actions a user can perform on this job
    job_actions = None

    def clone_as_draft(self, user):
        """
        Clones the dwf job for the user as a Draft MaryJob
        :param user: the owner of the new Draft MaryJob
        :return: Nothing
        """

        name = generate_draft_job_name(self.job, user)

        if not name:
            return None

        # Once the name is set, creating the draft job with new name and owner and same description
        cloned = MaryJob.objects.create(
            name=name,
            user=user,
            description=self.job.description,
        )

        # copying other parameters of the job
        clone_job_data(self.job, cloned)

        return cloned

    def list_actions(self, user):
        self.job_actions = list_job_actions(self.job, user)

    def __init__(self, job_id, light=False):
        """
        Initialises the DWF MaryJob
        :param job_id: id of the job
        :param light: Whether used for only job variable to be initialised atm
        """
        # do not need to do further processing for light dwf jobs
        # it is used only for status check mainly from the model itself to list the
        # actions a user can do on the job
        if light:
            return

        # populating job parameters tab information
        try:
            self.job_parameter = JobParameter.objects.get(job=self.job)
            self.job_parameters = self.get_job_parameters()
        except JobParameter.DoesNotExist:
            pass

    def __new__(cls, *args, **kwargs):
        """
        Instantiate the MaryJob
        :param args: arguments
        :param kwargs: keyword arguments
        :return: Instance of MaryJob with job variable initialised from job_id if exists
                 otherwise returns None
        """
        result = super(DwfMaryJob, cls).__new__(cls)
        try:
            result.job = MaryJob.objects.get(id=kwargs.get('job_id', None))
        except MaryJob.DoesNotExist:
            return None
        return result

    def get_job_parameters(self):
        """
        Generates an ordered dictionary of job parameters by skipping the required fields based on the template choice.
        :return: An ordered dictionary of job parameters
        """
        job_parameter_dict = OrderedDict()
        if self.job_parameter:
            fields = JobParameter._meta.get_fields()

            skip_fields = ['job', 'id', ]

            if self.job_parameter.template == JobParameter.OLD_TEMPLATE:
                skip_fields.append('mary_run_template')
                skip_fields.append('mary_run_template_sequence_number')
            elif self.job_parameter.template == JobParameter.NEW_TEMPLATE:
                skip_fields.append('old_template_name')
                skip_fields.append('template_date')

            for field in fields:
                if field.name not in skip_fields:
                    job_parameter_dict.update({
                        field.name: get_formatted_value_for_json(field, getattr(self.job_parameter, field.name)),
                    })
        return job_parameter_dict

    def as_json(self):
        """
        Generates the json representation of the MaryJob so that DWF Core can digest it
        :return: Json Representation
        """
        # accumulating all in one dict
        json_dict = dict(
            name=self.job.name,
            description=self.job.description,
            parameters=self.job_parameters,
        )

        # returning json with correct indentation
        return json.dumps(json_dict, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
