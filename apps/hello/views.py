from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.hello.models import MyInfo
from .model_instanse import create_instanse
#from django.views.generic.detail import DetailView

class HomeView(TemplateView):
    
    template_name = 'base.html'
    
    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        my_instanse = create_instanse()
        context['my_instanse'] = my_instanse
        return context




