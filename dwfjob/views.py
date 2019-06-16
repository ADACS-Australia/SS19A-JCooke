"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render

from .forms.mary_job.job import MaryJobForm
from .forms.mary_job.job_parameter import JobParameterForm


def new_job(request):
    if request.method == 'POST':
        job_form = MaryJobForm(request.POST, request=request, prefix='job')
        parameter_form = JobParameterForm(request.POST, user=request.user, prefix='parameter')

        if all([job_form.is_valid(), parameter_form.is_valid(), ]):
            job_created = job_form.save()

            # creating the form with job
            parameter_form = JobParameterForm(request.POST, user=request.user, job=job_created, prefix='parameter')
            parameter_form.save()

            action = request.POST.get('action', None)

            # if action == 'Submit':
            #     mary_job = MaryJob(job=job_created)

    else:
        job_form = MaryJobForm(prefix='job')
        parameter_form = JobParameterForm(prefix='parameter')

    parameter_form.update_fields_to_required()

    return render(
        request,
        "dwfjob/job_create.html",
        {
            'page_header': 'New',
            'forms': [job_form, parameter_form, ],
            'submit_and_save': True,
            'submit_text': 'Launch',
        }
    )


def dummy(request):
    return render(
        request,
        "dwfcommon/about.html"
    )
