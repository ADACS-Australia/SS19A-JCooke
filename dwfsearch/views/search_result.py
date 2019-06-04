"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import pickle
import codecs

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..utility.api import get_data
from ..utility.utils import get_search_columns


@login_required
def cone_search_result(request):

    try:
        query_parts = pickle.loads(codecs.decode(request.session['query_parts'].encode(), "base64"))
    except KeyError:
        query_parts = None

    if not query_parts:
        return redirect('cone_search')

    search_columns = get_search_columns(request.user)

    search_results, total = get_data(query_parts, search_columns)
    return render(
        request,
        "dwfsearch/cone_search_results.html",
        {
            'search_results': search_results,
        },
    )
