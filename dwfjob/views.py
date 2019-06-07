"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.shortcuts import render

from .forms.mary_job.mary_job import MaryJobForm


def new_job(request):
    if request.method == 'POST':
        form = MaryJobForm(request.POST, user=request.user)
        pass
    else:
        form = MaryJobForm()

    return render(
        request,
        "dwfjob/job_create.html",
        {
            'page_header': 'New',
            'form': form,
            'submit_text': 'Launch',
        }
    )


def dummy(request):
    return render(
        request,
        "dwfcommon/about.html"
    )
