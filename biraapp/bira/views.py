from rest_framework import status
from .serializers import IssueSerializer, ProjectlistSerializer
from .models import Projectlist, Issue, User
from django.http import JsonResponse
from rest_framework.decorators import api_view

#1)get_all_projects
def get_all_projects(request):
    try:
        projects = Projectlist.objects.all()
        data = list(projects.values("project_name","project_id","date_created","date_modified"))
        return JsonResponse(data,status=200,safe=False)
    except Projectlist.DoesNotExist:
        return JsonResponse('Projects exist', status=404)

#2)Get project details by id: get_project_details( project_id)
def get_project_details(request, project_id):
    try:
        project = Projectlist.objects.get(pk=project_id)
        serializer = ProjectlistSerializer(project)
        return JsonResponse(serializer.data,status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)

#3)create_issue(title, labels, assignee, type, sprint, status)
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

#4)get_all_issues_of_project(project_id)
def get_all_issues_of_project(request, project_assigned):
    try:
        issue = Issue.objects.filter(project_assigned=project_assigned)
        data = list(issue.values("issue_title", "type", "sprint", "status"))
        return JsonResponse(data,status=200,safe=False)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)

#6)Assign an issue to a user: assign_issue(issue_id, user_id)
def assign_user(request):
    try:
        issue = Issue.objects.get(issue_id=request.GET['issue_id'])
        user = User.objects.get(user_id=request.GET['user_id'])
        issue.assignee = user
        issue.save()
        serializer = IssueSerializer(issue)
        return JsonResponse(serializer.data,status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('assign user got failed', status=404)

#7)Get all issues assigned to the logged in user: get_issue_assigned_to_user( user_id)
def get_issues_by_user_id(request, user_id):
    try:
        issue = Issue.objects.filter(assignee=user_id)[:50]
        data = list(issue.values("issue_title", "type", "sprint", "status"))
        return JsonResponse({'data': data},status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('This project_id does not exist', status=404)

#8)Get all issues assigned to the logged in user: get_issue_assigned_to_user( user_id)
def update_issue_status(request):
    try:
        issue = Issue.objects.get(issue_id=request.GET['issue_id'])
        status = request.GET['status']
        issue.status = status
        issue.save()
        serializer = IssueSerializer(issue)
        return JsonResponse(serializer.data,status=200)
    except Projectlist.DoesNotExist:
        return JsonResponse('status update got failed', status=404)

def projects(request):
    project_list = Projectlist.objects.order_by('-date_created')[:50]
    output = ', '.join([p.project_name for p in project_list])
    return JsonResponse({'data': output})
