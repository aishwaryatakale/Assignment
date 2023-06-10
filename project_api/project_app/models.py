# project_api/project_app/models.py
from django.db import models

class Tenant(models.Model):
    # Define the fields for the Tenant model
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.name

class ProjectMetadata(models.Model):
    # Define the fields for the ProjectMetadata model
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    csv_file_location = models.CharField(max_length=255)
    model_evaluation_results = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Project Metadata - ID: {self.id}"
