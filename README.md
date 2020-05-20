# Django_ChatApplication
Djnago installation:
sudo pip install django
django-admin --version

Login Module steps:
- python manage.py startapp reg
- add reg in INSTALLED APP section in settings.py
- create templates folder under project
- add templates TEMPLATES section - 'DIRS':['templates'] in settings.py
- project.urls.py
    from django.urls import path, include
    urlpatterns = [ path('reg/', 'reg.urls') ]
- create urls.py under reg application
- To add built in login functionality to djnago => reg.urls.py
    from django.urls import path, include
    from django.contrib.auth.views import LoginView

    urlpatterns = [
    path('login/', LoginView.as_view())
    ]
- To access login module we have url : /reg/login/
- Create html template for login under templates folder : registration/login.html
- Let djnago database know about Login form, model name 'User'
    -python manage.py makemigrations
    -python manage.py migrate
- Create admin super user to login
    python manage.py createsuperuser
    test Test@123
- Add where the login should redirect in settings.py
    LOGIN_REDIRECT_URL = "/reg/reg/"
- To run application
    python manage.py runserver
    Launch url ex:http://127.0.0.1:3000/reg/login/
    Login using username and password

Logout module steps:
- To add built in logout functionality to djnago => reg.urls.py
    from django.contrib.auth.views import LogoutView
    urlpatterns = [
    path('logout/', LogoutView.as_view()),
    ]
- Create logout link on the html template
- Add where the login should redirect in settings.py
    LOGOUT_REDIRECT_URL = "/reg/login/"

Signup module steps:

- add signup link to html template -> registration/login.html
- create views for signup, add signup url and view name in reg/urls.py
    from reg.views import *
    urlpatterns = [ path('reg/', reg),]
- add forms.py under reg application
- utilize existing UserCreationForm form and User model to signup with additional fields in reg/forms.py
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User
- create signup view definition in reg/views.py
    from django.contrib.auth import authenticate,login
