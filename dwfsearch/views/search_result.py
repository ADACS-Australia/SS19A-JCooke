"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import pickle
import codecs

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from dwfcommon.utility.paginator import Paginator
from .. import constants
from ..utility.api import search
from ..utility.utils import (
    get_search_columns,
    search_display_headers,
)


@login_required
def cone_search_result(request):
    # checking for pagination to happen
    try:
        page = int(request.GET.get('page', None))

        # manually typing wrong page number will be barred.
        if page <= 0:
            return redirect(reverse('search_result') + '?page=1')

        offset = (page - 1) * constants.SEARCH_RESULT_PER_PAGE
    except (TypeError, ValueError):
        offset = 0

    try:
        query_parts = pickle.loads(codecs.decode(request.session['query_parts'].encode(), "base64"))
    except KeyError:
        query_parts = None

    if not query_parts:
        return redirect('cone_search')

    search_columns = get_search_columns(request.user)
    display_headers = search_display_headers(search_columns)
    search_results, total = search(query_parts, search_columns, constants.SEARCH_RESULT_PER_PAGE, offset)

    paginator = Paginator(start_index=offset + 1, total=total, per_page=constants.SEARCH_RESULT_PER_PAGE)

    return render(
        request,
        "dwfsearch/cone_search_results.html",
        {
            'search_results': search_results,
            'display_headers': display_headers,
            'paginator': paginator,
        },
    )
