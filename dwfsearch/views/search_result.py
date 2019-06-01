"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import pickle
import codecs

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..utils.api import get_data


@login_required
def cone_search_result(request):

    try:
        query_parts = pickle.loads(codecs.decode(request.session['query_parts'].encode(), "base64"))
    except KeyError:
        query_parts = None

    if not query_parts:
        return redirect('cone_search')

    search_results, total = get_data(query_parts)
    return render(
        request,
        "dwfsearch/cone_search_results.html",
        {
            'search_results': search_results,
        },
    )
