"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.urls import path

from .views import (
    cone_search,
)

urlpatterns = [
    path('search_result/', cone_search, name='cone_search_result'),
    path('', cone_search, name='cone_search'),
]
