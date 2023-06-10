# project_api/project_app/urls.py
from django.urls import path
from .views import TenantListCreateView, ProjectMetadataListCreateView

urlpatterns = [
    path('tenants/', TenantListCreateView.as_view(), name='tenant-list-create'),
    path('project-metadata/', ProjectMetadataListCreateView.as_view(), name='project-metadata-list-create'),
]
