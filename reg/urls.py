from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from reg.views import *
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('reg/', reg),
    path('signup/', signup),
]