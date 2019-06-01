"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import pickle
import codecs

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from dwfsearch.forms.cone_search.public import ConeSearchForm
from dwfsearch.forms.cone_search.collaborator import ConeSearchCollaboratorForm


@login_required
def cone_search(request):

    if request.method == 'POST':
        request.session['search_query'] = None

        form = ConeSearchCollaboratorForm(request.POST) \
            if request.user.is_collaborator \
            else ConeSearchForm(request.POST)

        if form.is_valid():
            query_parts = form.get_search_query()
            request.session['query_parts'] = codecs.encode(pickle.dumps(query_parts), "base64").decode()
            return redirect('cone_search_result')
    else:
        form = ConeSearchCollaboratorForm() \
            if request.user.is_collaborator \
            else ConeSearchForm()

        request.session['search_query'] = None

    return render(
        request,
        "dwfsearch/cone_search.html",
        {
            'form': form,
            'submit_text': 'Search',
        },
    )
