"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render

from .forms.mary_job.job import MaryJobForm
from .forms.mary_job.job_parameter import JobParameterForm


def new_job(request):
    if request.method == 'POST':
        job_form = MaryJobForm(request.POST, user=request.user, prefix='job')
        parameter_form = JobParameterForm(request.POST, user=request.user, prefix='parameter')

        if all([job_form.is_valid(), parameter_form.is_valid(), ]):
            pass

    else:
        job_form = MaryJobForm(prefix='job')
        parameter_form = JobParameterForm(prefix='parameter')

    return render(
        request,
        "dwfjob/job_create.html",
        {
            'page_header': 'New',
            'forms': [job_form, parameter_form, ],
            'submit_text': 'Launch',
        }
    )


def dummy(request):
    return render(
        request,
        "dwfcommon/about.html"
    )
