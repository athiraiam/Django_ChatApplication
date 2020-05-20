from django.urls import path
from home.views import *

urlpatterns = [
    path('search_user/', search_user)
]