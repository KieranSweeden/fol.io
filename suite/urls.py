"""
URL's for the pages related to the folio suite
"""

from django.urls import path
from . import views

urlpatterns = [
    path('open/', views.open_suite, name="open_suite"),
    path('open/<int:folio_id>/', views.open_suite, name="open_suite"),
    path('select/', views.select_folio, name="select_folio"),
    path('projects/',
         views.edit_folio_projects,
         name="edit_folio_projects"),
    path('projects/<int:folio_id>/',
         views.edit_folio_projects,
         name="edit_folio_projects"),
    path('projects/create/<int:folio_id>/',
         views.create_folio_project,
         name="create_folio_project"),
    path('projects/update/<int:folio_id>/<int:project_id>',
         views.update_folio_project,
         name="update_folio_project"),
    path('projects/update/projects_attached/<int:folio_id>/',
         views.update_projects_attached_to_folio,
         name="update_projects_attached_to_folio"),
    path('projects/delete/<int:folio_id>/<int:project_id>',
         views.delete_folio_project,
         name="delete_folio_project"),
    path('skills/<int:folio_id>/',
         views.edit_folio_skills,
         name="edit_folio_skills"),
    path('skills/',
         views.edit_folio_skills,
         name="edit_folio_skills"),
    path('profile/',
         views.edit_folio_profile,
         name="edit_folio_profile"),
    path('profile/<int:folio_id>/',
         views.edit_folio_profile,
         name="edit_folio_profile"),
    path('contact/',
         views.edit_folio_contact,
         name="edit_folio_contact"),
    path('contact/<int:folio_id>/',
         views.edit_folio_contact,
         name="edit_folio_contact"),
]
