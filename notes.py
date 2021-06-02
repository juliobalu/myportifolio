# Created a virtual environment in the CLI:
$ python3 venv .env

# Activated the virtual environment:
$ source .env/bin/activate

#Installed Django inside the virtual environment:
(.env)$ pip install django

# Created a Django project management app inside the existing folder without duplicating the folder structure:
# The dot avoids extra folders! 
(.env)$ django-admin startproject portfolio .

#start the server
(.env)$ python manage.py runserver

# Visited the site at http://localhost:8000

# Create a new app
(.env)$ python manage.py startapp projects

# It's necessary to add the app to settings.py (Project -> Main app / myportfolio/portfolio)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Here is where we add our apps.
    'projects'''

# In the main project url (portifolio\urls.py), it's necessary to add the app url:

from django.contrib import admin
from django.urls import include, path # <-- necessary to add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')) #<-- include the app
]

# In the app url (project\urls.py), it's necessary to point to the views of the app

from django.urls import path
from projects import views # <-- import the app views module

urlpatterns = [
    path('', views.project_list), # add all the app views here
]

# In the app view file (projects\view.py), instruct the view to render a template.

def project_list(request):
    return render(request, "projects/index.html")
	
# The template is a file with HTML command in a template folder:
# myportfolio/projects/template/projects/index.html

# Register your new template folder structure in settings.py:

import os # <- import module os
#
# ...
#
TEMPLATES = [
    {
	    'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'projects/templates')], #< -- add the app directories here
		'APP_DIRS': True,
    }
]

# Create the Migration class inside myportfolio/projects/migrations folder.
(.env)$ python manage.py makemigrations

# take the code you have and apply it to create or change the database that you’re working with
(.env)$ python manage.py migrate

# Start Python shell
(.env)$ python manage.py shell

>>> from projects.models import Project
>>> p1 = Project(title="Test Project", description="This is a test, 1234", technology="Django", image="project1.png")
>>> p1.save()
>>> results = Project.objects.all()
>>> results
<QuerySet [<Project: Project object (1)>]>
>>> p = results[0]
>>> p.title
'Test Project'
>>> p.description
'This is a test, 1234'
>>> p.technology
'Django'
>>> p.image
'project1.png'

# Django template language
{% cod logic %} # for loop, etc

{{ variables }} # print

# to link the detail page to the read more button:
<a href="{% url 'app_name:name' project.pk %}" >Read More</a>
#, where app_name and name can be found in urls.py


# To access the admin site it's necessary to create a superuser
(.env)$ python manage.py createsuperuser

# To add a project to the admin, import the modal an register it in the admin.py

from django.contrib import admin
from projects.models import Project # import


# Register your models here.
admin.site.register(Project) # register
