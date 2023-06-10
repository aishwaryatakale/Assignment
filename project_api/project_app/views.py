# project_api/project_app/views.py
from rest_framework import generics
from .models import Tenant, ProjectMetadata
from .serializers import TenantSerializer, ProjectMetadataSerializer

class TenantListCreateView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class ProjectMetadataListCreateView(generics.ListCreateAPIView):
    queryset = ProjectMetadata.objects.all()
    serializer_class = ProjectMetadataSerializer
