"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path

from .views.job import *
from .views.jobs import (
    public_jobs,
    jobs,
    all_jobs,
    drafts,
    all_drafts,
    deleted_jobs,
    all_deleted_jobs,
    view_job,
    edit_job,
    copy_job,
    make_job_private,
    make_job_public,
)

urlpatterns = [
    path('new_job/', new_job, name='new_job'),
    path('edit_job/<job_id>/', edit_job, name='edit_job'),
    path('cancel_job/<job_id>/', dummy, name='cancel_job'),
    path('copy_job/<job_id>/', copy_job, name='copy_job'),
    path('delete_job/<job_id>/', dummy, name='delete_job'),
    path('make_job_private/<job_id>/', make_job_private, name='make_job_private'),
    path('make_job_public/<job_id>/', make_job_public, name='make_job_public'),
    path('job/<job_id>/', view_job, name='job'),
    path('jobs/', jobs, name='jobs'),
    path('all_jobs/', all_jobs, name='all_jobs'),
    path('public_jobs/', public_jobs, name='public_jobs'),
    path('deleted_jobs/', deleted_jobs, name='deleted_jobs'),
    path('all_deleted_jobs/', all_deleted_jobs, name='all_deleted_jobs'),
    path('drafts/', drafts, name='drafts'),
    path('all_drafts/', all_drafts, name='all_drafts'),
]
