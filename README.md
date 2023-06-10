The goal of this application is to demonstrate a basic implementation of a machine learning workflow using Django, a popular Python web framework. The application performs the following steps:

1)It creates a new tenant entry in the database.
2)It reads the environment variables for the CSV file location and the target column name.
3)It builds a machine learning model using the data from the CSV file and the specified target column.
4)It saves the project metadata, including the CSV file location and the model evaluation results, in the database.
5)It fetches and prints the tenant and project metadata from the database.


Steps to execute locally :
Please make sure to clone this repo first.



1)Install the necessary dependencies:
	pip install Django djangorestframework pandas scikit-learn requests python-dotenv

2)Run database migrations:
	cd project_api
	python manage.py makemigrations
	python manage.py migrate

3)Set environment variables:
	Open the .env file in a text editor.
	Set the environment variables in the file as follows:

CSV_FILE_LOCATION=/path/to/data.csv
TARGET_COLUMN=<single column in csv file to evaluate>

4) Run the Django development server:
	python manage.py runserver

5) Execute the main script(entry point of the functionality):
	python main.py

6) Verify the results:
	Check the console output of the main script for the printed tenant and project metadata.
You can also access the Django API endpoints to view the stored data or use the Django admin interface if you have set it up.
	
