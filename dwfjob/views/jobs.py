"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from accounts.decorators import admin_or_system_admin_required
from dwfcommon.utility.utils import get_readable_size

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
@admin_or_system_admin_required
def all_jobs(request):
    """
    Collects all jobs that are not deleted or draft and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.all() \
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
            'admin_view': True,
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


@login_required
def deleted_jobs(request):
    """
    Collects all deleted jobs of the user and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.filter(Q(user=request.user), Q(job_status__in=[JobStatus.DELETED, ])) \
        .order_by('-last_updated', '-creation_time')

    paginator = Paginator(my_jobs, JOBS_PER_PAGE)

    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    # creating mary jobs from jobs
    # it will create a light job with list of actions this user can do based on the job status
    mary_jobs = []
    for job in job_list:
        mary_job = DwfMaryJob(job_id=job.id, light=True)
        mary_job.list_actions(request.user)
        mary_jobs.append(mary_job)

    return render(
        request,
        "dwfjob/all-jobs.html",
        {
            'jobs': mary_jobs,
            'deleted': True,
        }
    )


@login_required
@admin_or_system_admin_required
def all_deleted_jobs(request):
    """
    Collects all deleted jobs and renders them in template.
    :param request: Django request object.
    :return: Rendered template.
    """

    my_jobs = MaryJob.objects.filter(Q(job_status__in=[JobStatus.DELETED, ])) \
        .order_by('-last_updated', '-creation_time')

    paginator = Paginator(my_jobs, JOBS_PER_PAGE)

    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    # creating mary jobs from jobs
    # it will create a light job with list of actions this user can do based on the job status
    mary_jobs = []
    for job in job_list:
        mary_job = DwfMaryJob(job_id=job.id, light=True)
        mary_job.list_actions(request.user)
        mary_jobs.append(mary_job)

    return render(
        request,
        "dwfjob/all-jobs.html",
        {
            'jobs': mary_jobs,
            'deleted': True,
            'admin_view': True,
        }
    )


@login_required
def view_job(request, job_id):
    """
    Collects a particular job information and renders them in template.
    :param request: Django request object.
    :param job_id: id of the job.
    :return: Rendered template.
    """

    job = None

    # checking:
    # 1. Job ID and job exists
    if job_id:
        try:
            job = MaryJob.objects.get(id=job_id)

            # Check that this user has access to this job
            # it can view if there is a copy access
            mary_job = DwfMaryJob(job_id=job.id, light=False)
            mary_job.list_actions(request.user)

            if 'copy' not in mary_job.job_actions:
                job = None
            else:
                # Empty parameter dict to pass to template
                job_data = {
                    'L1': None,
                    'V1': None,
                    'H1': None,
                    'corner': None,
                    'archive': None,
                    # for drafts there are no clusters assigned, so mary_job.job.custer is None for them
                    'is_online': mary_job.job.cluster is not None and mary_job.job.cluster.is_connected() is not None
                }

                # Check if the cluster is online
                if job_data['is_online']:
                    try:
                        # Get the output file list for this job
                        result = mary_job.job.fetch_remote_file_list(path="/", recursive=True)
                        # Waste the message id
                        result.pop_uint()
                        # Iterate over each file
                        num_entries = result.pop_uint()
                        for _ in range(num_entries):
                            path = result.pop_string()
                            # Waste the is_file bool
                            result.pop_bool()
                            # Waste the file size
                            size = get_readable_size(result.pop_ulong())

                            # Check if this is a wanted file
                            if 'output/L1_frequency_domain_data.png' in path:
                                job_data['L1'] = {'path': path, 'size': size}
                            if 'output/V1_frequency_domain_data.png' in path:
                                job_data['V1'] = {'path': path, 'size': size}
                            if 'output/H1_frequency_domain_data.png' in path:
                                job_data['H1'] = {'path': path, 'size': size}
                            if 'output/mary_corner.png' in path:
                                job_data['corner'] = {'path': path, 'size': size}
                            if 'mary_job_{}.tar.gz'.format(mary_job.job.id) in path:
                                job_data['archive'] = {'path': path, 'size': size}
                    except:
                        job_data['is_online'] = False

                return render(
                    request,
                    "dwfjob/view_job.html",
                    {
                        'mary_job': mary_job,
                        'job_data': job_data
                    }
                )
        except MaryJob.DoesNotExist:
            pass

    if not job:
        # should return to a page notifying that no permission to view
        raise Http404
