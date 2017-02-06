from apps.requests_history.models import RequestHistory
from django.shortcuts import render


class RequestHistoryMiddleware():
    def process_request(self, request):
        try:
            instanse = RequestHistory.objects.create(request_method = request.method,request_lenght = request.META['HTTP_REFERER'])
        except KeyError :
            instanse = RequestHistory.objects.create(request_method = request.method,request_lenght = "None")
        my_instanse = RequestHistory.objects.order_by('-request_time')
        for c in range(len(my_instanse)):
        	if c >= 10:
        		my_instanse[c].delete()
        return None
