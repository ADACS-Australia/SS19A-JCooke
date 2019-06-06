"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from ..models import (
    SearchColumn,
    CoreMemberSearchColumn,
    PublicSearchColumn,
    CollaboratorSearchColumn,
)


class DisplayHeader(object):
    def __init__(self, name, display_name, sort_order=''):
        self.name = name
        self.display_name = display_name
        self.sort_order = sort_order


def reset_session(request):
    request.session['search_query'] = None
    request.session['display_headers'] = None


def get_search_columns(user):
    if not user:
        return []

    try:
        if user.is_admin:
            search_columns = CoreMemberSearchColumn.objects.values_list('column__name', flat=True) \
                .order_by('display_order')
        elif user.is_collaborator:
            search_columns = CollaboratorSearchColumn.objects.values_list('column__name', flat=True) \
                .order_by('display_order')
        else:
            search_columns = PublicSearchColumn.objects.values_list('column__name', flat=True) \
                .order_by('display_order')
    except (
            CoreMemberSearchColumn.DoesNotExist,
            CollaboratorSearchColumn.DoesNotExist,
            PublicSearchColumn.DoesNotExist,
    ):
        search_columns = []

    return search_columns


def search_display_headers(search_columns):
    display_headers = []

    for column in search_columns:
        try:
            display_headers.append(
                DisplayHeader(
                    name=column,
                    display_name=SearchColumn.objects.get(name=column).display_name,
                )
            )
        except SearchColumn.DoesNotExist:
            pass

    return display_headers


def process_search_results(search_result, search_columns):
    processed_result = []

    for result in search_result:
        sorted_result = []
        for column in search_columns:
            sorted_result.append(result.get(column, None))
        processed_result.append(sorted_result)

    return processed_result
