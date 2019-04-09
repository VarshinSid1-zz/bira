from rest_framework import generics
from django.shortcuts import render
from .serializers import ProjectlistSerializer
from .models import Projectlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Projectlist.objects.all()
    serializer_class = ProjectlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Projectlist.objects.all()
    serializer_class = ProjectlistSerializer