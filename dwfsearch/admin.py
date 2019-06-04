"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib import admin

from .models import (
    SearchColumn,
    PublicSearchColumn,
    CollaboratorSearchColumn,
    CoreMemberSearchColumn,
)


@admin.register(SearchColumn)
class SearchColumn(admin.ModelAdmin):
    list_display = ('name', 'display_name',)
    search_fields = ['name', 'display_name', ]


@admin.register(PublicSearchColumn)
class PublicSearchColumn(admin.ModelAdmin):
    list_display = ('column', 'display_order',)
    search_fields = ['column__name', 'column__display_name', ]


@admin.register(CollaboratorSearchColumn)
class CollaboratorSearchColumn(admin.ModelAdmin):
    list_display = ('column', 'display_order',)
    search_fields = ['column__name', 'column__display_name', ]


@admin.register(CoreMemberSearchColumn)
class CoreMemberSearchColumn(admin.ModelAdmin):
    list_display = ('column', 'display_order',)
    search_fields = ['column__name', 'column__display_name', ]
