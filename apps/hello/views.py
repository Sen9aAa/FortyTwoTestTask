from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from apps.hello.models import MyInfo
from apps.requests_history.models import RequestHistory
from django.http import HttpResponse
import datetime
from django import forms
import json
from widget import DateWidget
from imagefield_widget import ImageFieldWidget
import os, sys
from PIL import Image
#from django.views.generic.detail import DetailView

class HomeView(TemplateView):
    
    template_name = 'index.html'
    
    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        my_instanse = MyInfo.objects.all()
        requests_instanse = RequestHistory.objects.all()
        requests_number = 0
        for c in requests_instanse:
            if c.request_status == 0:
                requests_number+=1
        context['my_instanse'] = my_instanse
        context['requests_number'] = requests_number
        return context

class My_add_data_form(forms.ModelForm):
    class Meta:
        model = MyInfo
        fields = '__all__'
        widgets={'birthday':DateWidget(usel10n=True, bootstrap_version=3),
                  'photo':ImageFieldWidget}

    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        instanse = (datetime.date.today() - data).days/364.0
        if instanse > 120 :
            raise forms.ValidationError('You alredy dead now')
        if instanse <=0:
            raise forms.ValidationError('You not born yeat')
        return data

        


def my_add_data_form(request,info_id = None):
    args={}
    my_instanse = None
    my_id = None
    if info_id != None:
        my_instanse = MyInfo.objects.get(id = info_id)
        my_id = my_instanse.id
    if request.method =='POST':
        form = My_add_data_form(request.POST,request.FILES,instance = my_instanse)
        if form.is_valid():
            my_instanse = form.save()
            if int(request.POST['img_clear']) == 1:
                my_instanse.photo = ''
                my_instanse.save()
            if my_id!= None:
                args['ok_message'] = 'Data has been change'
            else:
                args['ok_message'] = 'A new info has been added'
            return HttpResponse(json.dumps(args), content_type= "application/json")
        elif form.errors:
            return HttpResponse(json.dumps(form.errors),content_type = "application/json")
    else:
        form = My_add_data_form(instance=my_instanse)
    return render(request,'Add_data.html',{'form':form,'my_id':my_id})


def my_delete(request,my_info_id):
    info = MyInfo.objects.get(id = my_info_id)
    info.delete()
    return redirect('home')