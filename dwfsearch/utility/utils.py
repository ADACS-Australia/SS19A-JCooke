"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from .. import constants


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

    if user.is_admin:
        search_columns = constants.ADMIN_SEARCH_COLUMNS
    elif user.is_collaborator:
        search_columns = constants.COLLABORATOR_SEARCH_COLUMNS
    else:
        search_columns = constants.PUBLIC_SEARCH_COLUMNS

    return search_columns


def search_display_headers(search_columns):
    display_headers = []

    for column in search_columns:
        display_headers.append(
            DisplayHeader(
                name=column,
                display_name=constants.SEARCH_DISPLAY_HEADERS.get(column, column),
            )
        )

    return display_headers
