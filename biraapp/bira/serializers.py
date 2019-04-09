from rest_framework import serializers
from .models import Projectlist


class ProjectlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Projectlist
        fields = ('project_id', 'project_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')