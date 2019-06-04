"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from ..models import (
    CoreMemberSearchColumn,
    PublicSearchColumn,
    CollaboratorSearchColumn,
)


def get_search_columns(user):
    if not user:
        return []

    try:
        if user.is_admin:
            search_columns = CoreMemberSearchColumn.objects.values_list('name', flat=True).order_by('display_order')
        elif user.is_collaborator:
            search_columns = CollaboratorSearchColumn.objects.values_list('name', flat=True).order_by('display_order')
        else:
            search_columns = PublicSearchColumn.objects.values_list('name', flat=True).order_by('display_order')
    except (
            CoreMemberSearchColumn.DoesNotExist,
            CollaboratorSearchColumn.DoesNotExist,
            PublicSearchColumn.DoesNotExist,
    ):
        search_columns = []

    return search_columns
