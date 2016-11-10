from django.shortcuts import render
from django.views.generic.base import TemplateView


class RequestHistory(TemplateView):     

    template_name = 'request_history.html'
    
    


