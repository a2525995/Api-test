from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from requestnew.models import *
import logging
from public.utils import check_email, check_phone, sha_256
# Create your views here.

log = logging.getLogger(__file__)


def accept_message(request):
    data = {
        "msg": "ok",
        "result": "1"
    }
    log.info("123")
    return JsonResponse(data, status=200)

#
def get_model(request):
    #obj = UserInfo.objects.all().values()
    obj = []
    print(obj)
    obj = list(obj)
    print(type(obj[1]))
    d = {
        "test": obj
    }
    return JsonResponse(data=d, safe=False)


