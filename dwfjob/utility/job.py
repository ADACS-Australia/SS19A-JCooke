"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import json

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

    def as_json(self):
        """
        Generates the json representation of the MaryJob so that DWF Core can digest it
        :return: Json Representation
        """

        # processing data dict
        job_parameter_dict = dict()
        if self.job_parameter:
            fields = JobParameter._meta.get_fields()

            for field in fields:
                if field.name not in ['job', 'id', ]:
                    job_parameter_dict.update({
                        field.name: get_formatted_value_for_json(field, getattr(self.job_parameter, field.name)),
                    })

        # accumulating all in one dict
        json_dict = dict(
            name=self.job.name,
            description=self.job.description,
            parameter=job_parameter_dict,
        )

        # returning json with correct indentation
        return json.dumps(json_dict, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
