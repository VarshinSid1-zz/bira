from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_project_details, get_all_projects, projects, create_issue, get_all_issues_of_project, \
    assign_user, get_issues_by_user_id, update_issue_status
from django.urls import path

urlpatterns = {
    path("projects/", get_all_projects, name="get_all_projects"),
    path("project/id/<str:project_id>/", get_project_details, name="get_project_details"),
    path("createissue/", create_issue, name="create_issue"),
    path("issue/id/<str:project_assigned>/", get_all_issues_of_project, name="get_all_issues_of_project"),
    path("update_issue/", assign_user, name="assign_user"),
    path("issue/userid/<str:user_id>/", get_issues_by_user_id, name="get_issues_by_user_id"),
    path("update_issue_status/", update_issue_status, name="update_issue_status"),
    path("projectlists/", projects, name="projects"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

