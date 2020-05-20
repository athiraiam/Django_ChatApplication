from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.models import User
# Create your views here.

def search_user(request):
    if 'title' in request.GET:
        all_users=[]
        user_details = User.objects.get(username__exact= request.GET.get('title'))
        username = user_details.username
        first_name = user_details.first_name
        last_name = user_details.last_name
        SearchModel.objects.create(username= username, first_name= first_name, last_name=last_name)
        all_details = SearchModel.objects.all()
        for i in all_details:
            all_users.append(i.username)
        all_users =set(all_users)
        print(all_users)
    return render(request, "home/search_user.html", {'all_users': all_users})