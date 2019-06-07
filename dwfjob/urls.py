"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('new_job/', login_required(new_job), name='new_job'),
    path('edit_job/<job_id>/', login_required(dummy), name='edit_job'),
    path('cancel_job/<job_id>/', login_required(dummy), name='cancel_job'),
    path('copy_job/<job_id>/', login_required(dummy), name='copy_job'),
    path('delete_job/<job_id>/', login_required(dummy), name='delete_job'),
    path('make_job_private/<job_id>/', login_required(dummy), name='make_job_private'),
    path('make_job_public/<job_id>/', login_required(dummy), name='make_job_public'),
    path('job/<job_id>/', login_required(dummy), name='job'),
    path('jobs/', dummy, name='jobs'),
    path('all_jobs/', dummy, name='all_jobs'),
    path('public_jobs/', dummy, name='public_jobs'),
    path('deleted_jobs/', dummy, name='deleted_jobs'),
    path('all_deleted_jobs/', dummy, name='all_deleted_jobs'),
    path('drafts/', dummy, name='drafts'),
    path('all_drafts/', dummy, name='all_drafts'),
]
