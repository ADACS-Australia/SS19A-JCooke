"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms.cone_search.public import ConeSearchForm
from .forms.cone_search.collaborator import ConeSearchCollaboratorForm


@login_required
def cone_search(request):

    if request.method == 'POST':
        form = ConeSearchCollaboratorForm(request.POST) \
            if request.user.is_collaborator \
            else ConeSearchForm(request.POST)
    else:
        form = ConeSearchCollaboratorForm() \
            if request.user.is_collaborator \
            else ConeSearchForm()

    return render(
        request,
        "dwfsearch/cone_search.html",
        {
            'form': form,
            'submit_text': 'Search',
        },
    )
