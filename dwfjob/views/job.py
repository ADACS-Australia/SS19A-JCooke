"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from django_hpc_job_controller.client.scheduler.status import JobStatus

from ..forms.mary_job.job import MaryJobForm
from ..forms.mary_job.job_parameter import JobParameterForm
from ..utility.job import DwfMaryJob
from ..models import MaryJob


@login_required
def new_job(request):
    if request.method == 'POST':

        to_load_job = None
        if request.session['draft_job']:
            try:
                to_load_job = MaryJob.objects.get(id=request.session['draft_job'].get('id', None))
            except MaryJob.DoesNotExist:
                pass

        job_form = MaryJobForm(request.POST, request=request, job=to_load_job, prefix='job')
        parameter_form = JobParameterForm(request.POST, user=request.user, prefix='parameter')

        if all([job_form.is_valid(), parameter_form.is_valid(), ]):
            job_created = job_form.save()

            # creating the form with job
            parameter_form = JobParameterForm(request.POST, user=request.user, job=job_created, prefix='parameter')
            parameter_form.save()

            action = request.POST.get('action', None)

            if action == 'Launch':
                mary_job_json = DwfMaryJob(job_id=job_created.id).as_json()
                # the json representation of the job is to be saved in the Job model
                job_created.json_representation = mary_job_json

                try:
                    # Submit the job to HPC
                    job_created.submit(mary_job_json)
                except:
                    pass
                else:
                    return redirect('jobs')
            elif action == 'Save':
                return redirect('drafts')

    else:

        editing_draft = False

        try:
            request.session['draft_job'] = request.session['to_load']
        except (AttributeError, KeyError):
            request.session['draft_job'] = None

        if request.session['draft_job']:
            try:
                to_load_job = MaryJob.objects.get(id=request.session['draft_job'].get('id', None))
                editing_draft = True
            except MaryJob.DoesNotExist:
                to_load_job = None

            request.session['to_load'] = None
        else:

            to_load_job = MaryJob.objects\
                .filter(~Q(job_status__in=[JobStatus.DRAFT, ]))\
                .order_by('-job_pending_time').first()

        job_form = MaryJobForm(
            prefix='job',
            job=to_load_job,
            editing_draft=editing_draft,
        )
        parameter_form = JobParameterForm(
            prefix='parameter',
            job=to_load_job,
        )

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
