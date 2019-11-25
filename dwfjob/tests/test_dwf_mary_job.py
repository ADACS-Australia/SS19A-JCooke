"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import json

from django.test import TestCase

from dwfcommon.tests.utils import TestData

from ..models import JobParameter, MaryJob
from ..utility.job import DwfMaryJob


class TestJSONRepresentation(TestCase):
    """
    Class to test json representation of DWF Mary job is correct
    """

    @classmethod
    def setUpTestData(cls):
        cls.data = TestData()
        cls.data.create_public_users()
        cls.data.create_collaborators()
        cls.data.create_core_members()

    def test_full_json_old_template(self):
        """
        tests to checkout a fully qualified json format of Mary Job
        :return: Nothing
        """

        expected_data = {
            "description": None,
            "name": "test job",
            "parameters": {
                "clobber": "True",
                "date": "190621",
                "field": "some/a field",
                "filter": "g Band",
                "mary_seed_name": "rt",
                "old_template_name": "my old template",
                "steps": 20,
                "template": "old_template",
                "template_date": "190611",
                "image_names": "",
                "run_dates": "190507, 190505",
            }
        }

        mary_job = MaryJob.objects.create(
            user=self.data.core_members[0],
            name='test job',
        )

        JobParameter.objects.create(
            job=mary_job,
            field='some/a field',
            date='190621',  # it will be saved as UTC
            template='old_template',
            template_date='190611',
            mary_seed_name='rt',
            steps=20,
            clobber='True',
            filter='g Band',
            old_template_name='my old template',
            mary_run_template=None,
            mary_run_template_sequence_number=None,
            run_dates='190507, 190505',
        )

        dwf_mary_job = DwfMaryJob(job_id=mary_job.id)

        self.assertJSONEqual(json.dumps(expected_data, indent=4, sort_keys=True), dwf_mary_job.as_json())
