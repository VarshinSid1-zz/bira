from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_project_by_id, projects_list, projects, create_issue
from django.urls import path

urlpatterns = {
    path("projects/", projects_list, name="projects_list"),
    path("projectlists/", projects, name="projects"),
    path("project/id/<str:project_id>/", get_project_by_id, name="get_project_by_id"),
    path("createissue/", create_issue, name="create_issue"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

