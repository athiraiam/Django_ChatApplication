from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from reg.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="/reg/login/")
def reg(request):
    profile_info = User.objects.get(username = str(request.user))
    profile_first = profile_info.first_name
    profile_last = profile_info.last_name
    return render(request, "registration/reg.html", {'profile_first': profile_first, 'profile_last':profile_last})
def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect("/reg/reg/")
    return render(request,"registration/signup.html", {'form':form})

