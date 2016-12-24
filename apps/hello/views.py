from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.hello.models import MyInfo
from apps.requests_history.models import RequestHistory
from django.http import HttpResponse
from django import forms
import json
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


def my_add_data_form(request):
    args={}
    if request.method =='POST':
        form = My_add_data_form(request.POST)
        if form.is_valid():
            form.save()
            args['ok_message'] = 'A new info has been added'
            return HttpResponse(json.dumps(args), content_type= "application/json")
        elif form.errors:
            return HttpResponse(json.dumps(form.errors),content_type = "application/json")
    else:
        form = My_add_data_form()
    return render(request,'Add_data.html',{'form':form})

 