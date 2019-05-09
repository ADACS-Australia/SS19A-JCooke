"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
