# project_api/project_app/serializers.py
from rest_framework import serializers
from .models import Tenant, ProjectMetadata

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class ProjectMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMetadata
        fields = '__all__'
