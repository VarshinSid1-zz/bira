from rest_framework import status
from .serializers import IssueSerializer
from .models import Projectlist, Issue
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view


def projects_list(request):
    try:
        projects = Projectlist.objects.all()
        data = list(projects.values("project_name","project_id","date_created","date_modified"))
        return HttpResponse(data, status=200)
    except Projectlist.DoesNotExist:
        return HttpResponse('Projects exist', status=404)


def get_project_by_id(request, project_id):
    try:
        project = Projectlist.objects.filter(pk=project_id)
        data = list(project.values("project_name"))
        return HttpResponse(data, status=200)
    except Projectlist.DoesNotExist:
        return HttpResponse('This project_id does not exist', status=404)


def projects(request):
    project_list = Projectlist.objects.order_by('project_name')[:3]
    output = ', '.join([p.project_name for p in project_list])
    return HttpResponse(output)


@api_view(['GET','POST'])
def create_issue(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return HttpResponse(serializer.data)
    elif request.method == 'POST':
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

