from rest_framework import serializers
from .models import Projectlist, Issue


class ProjectlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Projectlist
        fields = ('project_id', 'project_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('issue_id', 'issue_title', 'assignee', 'project_assigned', 'type', 'sprint', 'status')