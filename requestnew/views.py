from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from requestnew.models import *
import logging
# Create your views here.

log = logging.getLogger("requestnew")

def login(request):
    if request.method == 'GET':
        print("123")
    return render(request, 'index.html')

def accept_message(request):
    data = {
        "msg": "ok",
        "result": "1"
    }
    log.info("123")
    return JsonResponse(data, status=200)


def get_model(request):
    obj = Student.objects.all().values_list('sid', flat=True)

    print(obj)
    obj = list(obj)
    print(type(obj[1]))
    d = {
        "test": obj
    }
    return JsonResponse(data=d, safe=False)



