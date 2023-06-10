# This is main.py which is a entry point for our project
import os
import django
from dotenv import load_dotenv
from ml_component.model_builder import build_model
import sys


# Adding the project directory to the sys.path
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project_api')
sys.path.append(project_dir)

# Set up Django
# Note: Modify second parameter when sys.path is changed
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_api.settings")
django.setup()

# Load environment variables
load_dotenv()

# Import Django models
from project_app.models import Tenant, ProjectMetadata


def create_tenant(name):
    tenant = Tenant.objects.create(name=name)
    return tenant

def save_project_metadata(tenant, csv_file_location, model_evaluation_results):
    project_metadata = ProjectMetadata.objects.create(
        tenant=tenant,
        csv_file_location=csv_file_location,
        model_evaluation_results=model_evaluation_results
    )
    return project_metadata

def fetch_tenant_and_metadata():
    tenants = Tenant.objects.all()
    project_metadata = ProjectMetadata.objects.all()
    return tenants, project_metadata

if __name__ == "__main__":
    # Create a tenant entry
    tenant = create_tenant("My Tenant")
    

    # Reading environment variables
    csv_file_location = os.environ.get("CSV_FILE_LOCATION")
    target_column = os.environ.get("TARGET_COLUMN")

    # Build the model
    model, score = build_model(csv_file_location, target_column)

    # Save project metadata
    project_metadata = save_project_metadata(tenant, csv_file_location, score)

    # Fetch and print tenant and project metadata
    tenants, metadata = fetch_tenant_and_metadata()
    print("Tenants:")
    for t in tenants:
        print(t.name)
    print("Project Metadata:")
    for m in metadata:
        print(m.csv_file_location, m.model_evaluation_results)
