from rest_framework import status
from .serializers import IssueSerializer
from .models import Projectlist, Issue
from django.http import JsonResponse
from rest_framework.decorators import api_view


def projects_list(request):
    try:
        projects = Projectlist.objects.all()
        data = list(projects.values("project_name","project_id","date_created","date_modified"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('Projects exist', status=404)


def get_project_by_id(request, project_id):
    try:
        project = Projectlist.objects.filter(pk=project_id)
        data = list(project.values("project_name"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)


def projects(request):
    project_list = Projectlist.objects.order_by('-date_created')[:50]
    output = ', '.join([p.project_name for p in project_list])
    return JsonResponse({'data': output})


@api_view(['GET','POST'])
def create_issue(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return JsonResponse({"data": serializer.data}, status=200)
    elif request.method == 'POST':
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_issues_by_id(request, project_assigned):
    try:
        issue = Issue.objects.filter(project_assigned=project_assigned)
        data = list(issue.values("issue_title", "type", "sprint", "status"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)

def get_issues_by_user_id(request, user_id):
    try:
        issue = Issue.objects.filter(assignee=user_id)[:50]
        data = list(issue.values("issue_title", "type", "sprint", "status"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)

def assign_user(request, issue_id, user_id):
    try:
        issue = Issue.objects.filter(project_assigned=issue_id)
        data = list(issue.values("issue_title", "type", "sprint", "status"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)