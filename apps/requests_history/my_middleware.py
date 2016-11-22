from apps.requests_history.models import RequestHistory
from django.shortcuts import render


class RequestHistoryMiddleware :
    def process_request(self, request):
        try:
            instanse = RequestHistory.objects.create(request_method = request.method,request_lenght = request.META['HTTP_REFERER'])
        except KeyError :
            instanse = RequestHistory.objects.create(request_method = request.method,request_lenght = "None")
        my_instanse = RequestHistory.objects.order_by('-request_time')
        if len(my_instanse) > 10:
            my_instanse[len(my_instanse)-1].delete()
        return None
