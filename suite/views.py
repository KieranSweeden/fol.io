"""
Views for the pages related to the folio suite
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_folio_projects(request):
    """
    Presents the projects tab of the
    folio to the user.
    """

    return render(request, "suite/edit_projects.html")


@login_required
def view_folio_skills(request):
    """
    Presents the skills tab of the
    folio to the user.
    """

    return render(request, "suite/edit_skills.html")


@login_required
def view_folio_profile(request):
    """
    Presents the profile tab of the
    folio to the user.
    """

    return render(request, "suite/edit_profile.html")

@login_required
def view_folio_contact(request):
    """
    Presents the contact tab of the
    folio to the user.
    """

    return render(request, "suite/edit_contact.html")

