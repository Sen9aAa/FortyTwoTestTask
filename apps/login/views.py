from django.shortcuts import render,redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import HttpResponse
import json

class MyLoginView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'


def my_registration(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            form.save()
            return HttpResponse(json.dumps({'new_user':'New User has been created'}),content_type ="application/json")
        if form.errors:
            my_errors = form.errors
            return HttpResponse(json.dumps(my_errors),content_type="application/json")
    else:
        form = UserCreationForm()
        return render(request,'registration.html',{'form':form})



