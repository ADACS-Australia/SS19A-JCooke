"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from accounts.decorators import admin_or_system_admin_required

from ..utility.constants import JOBS_PER_PAGE
from ..utility.job import DwfMaryJob
from ..models import MaryJob, JobStatus


@login_required
def jobs(request):
    """
    Collects all jobs that are not draft or deleted and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.filter(user=request.user) \
        .exclude(job_status__in=[JobStatus.DRAFT, JobStatus.DELETED]) \
        .order_by('-last_updated', '-job_pending_time')

    paginator = Paginator(my_jobs, JOBS_PER_PAGE)

    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    # creating mary jobs from jobs
    # it will create a light job with list of actions this user can do based on the job status
    mary_jobs = []
    for job in job_list:
        mary_job = DwfMaryJob(job_id=job.id, light=True)

        if mary_job:
            mary_job.list_actions(request.user)
            mary_jobs.append(mary_job)

    return render(
        request,
        "dwfjob/all-jobs.html",
        {
            'jobs': mary_jobs,
        }
    )


@login_required
def drafts(request):
    """
    Collects all drafts of the user and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.filter(Q(user=request.user), Q(job_status__in=[JobStatus.DRAFT, ])) \
        .exclude(job_status__in=[JobStatus.DELETED, ]) \
        .order_by('-last_updated', '-creation_time')

    paginator = Paginator(my_jobs, JOBS_PER_PAGE)

    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    # creating mary jobs from jobs
    # it will create a light job with list of actions this user can do based on the job status
    mary_jobs = []
    for job in job_list:
        mary_job = DwfMaryJob(job_id=job.id, light=True)

        if mary_job:
            mary_job.list_actions(request.user)
            mary_jobs.append(mary_job)

    return render(
        request,
        "dwfjob/all-jobs.html",
        {
            'jobs': mary_jobs,
            'drafts': True,
        }
    )


@login_required
@admin_or_system_admin_required
def all_drafts(request):
    """
    Collects all drafts and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.filter(Q(job_status__in=[JobStatus.DRAFT, ])) \
        .exclude(job_status__in=[JobStatus.DELETED, ]) \
        .order_by('-last_updated', '-creation_time')

    paginator = Paginator(my_jobs, JOBS_PER_PAGE)

    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    # creating mary jobs from jobs
    # it will create a light job with list of actions this user can do based on the job status
    mary_jobs = []
    for job in job_list:
        mary_job = DwfMaryJob(job_id=job.id, light=True)

        if mary_job:
            mary_job.list_actions(request.user)
            mary_jobs.append(mary_job)

    return render(
        request,
        "dwfjob/all-jobs.html",
        {
            'jobs': mary_jobs,
            'drafts': True,
            'admin_view': True,
        }
    )
