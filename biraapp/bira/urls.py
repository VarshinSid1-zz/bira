from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_project_by_id, projects_list, projects, create_issue, get_issues_by_id, assign_user,\
        get_issues_by_user_id
from django.urls import path

urlpatterns = {
    path("projects/", projects_list, name="projects_list"),
    path("projectlists/", projects, name="projects"),
    path("project/id/<str:project_id>/", get_project_by_id, name="get_project_by_id"),
    path("createissue/", create_issue, name="create_issue"),
    path("issue/id/<str:project_assigned>/", get_issues_by_id, name="get_issues_by_id"),
    path("issue/userid/<str:user_id>/", get_issues_by_user_id, name="get_issues_by_user_id"),
    path("issue/id/<str:issue_id>/<str:user_id>/", assign_user, name="assign_user"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

