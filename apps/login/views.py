from django.shortcuts import render,redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse
import json


def my_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            form.save()
            user = auth.authenticate(username = username,password = password)
            auth.login(request,user)
            return HttpResponse(json.dumps({'new_user':'New User has been created'}),content_type ="application/json")
        if form.errors:
            my_errors = form.errors
            return HttpResponse(json.dumps(my_errors),content_type="application/json")
    else:
        form = UserCreationForm()
        return render(request,'registration.html',{'form':form})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            new_user = {'username':user.username}
            return HttpResponse(json.dumps(new_user),content_type  = "application/json")
        else:
            my_errors = {'user_error':"Your username and password didn't match."}
            return HttpResponse(json.dumps(my_errors),content_type  = "application/json")

def my_logout(request):
    logout_content = {'bay':'Bay bay %s'%(request.user.username)}
    auth.logout(request)
    return HttpResponse(json.dumps(logout_content),content_type = "application/json")