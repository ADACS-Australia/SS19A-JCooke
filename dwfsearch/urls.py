"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path

from .views.search import cone_search
from .views.search_result import cone_search_result

urlpatterns = [
    path('search_result/', cone_search_result, name='cone_search_result'),
    path('', cone_search, name='cone_search'),
]
