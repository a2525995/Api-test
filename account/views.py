from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from public.utils import *
from .models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.views.generic import TemplateView
# Create your views here.

logger = logging.getLogger(__file__)


def get_index(request):
    return render(request, 'account/index.html')

def get_register(request):
    return render(request, 'account/register.html')

@require_http_methods(['POST'])
def register(request):
    username = request.POST.get('form-username')
    password = request.POST.get('form-password')
    email = request.POST.get('form-email')
    phone = request.POST.get('form-phone')

    #如果任意一项为空，则返回注册页面
    if not all([username, password, email, phone]):
        return HttpResponseRedirect(reverse('main'))

    #如果邮箱不符合正则表达式，返回注册页面
    if not check_email(email):
        return get_register(request)

    # 如果手机不符合正则表达式，返回注册页面
    if not check_phone(phone):
        return get_register(request)

    #检测邮箱
    user_email = User.objects.filter(email__exact=email)
    if user_email:
        return HttpResponseRedirect(reverse('register'))

    #检测手机
    user_phone = User.objects.filter(phone__exact=phone)
    if user_phone:
        return HttpResponseRedirect(reverse('register'))

    #检测用户名
    user = User.objects.filter(username__exact=username)
    if user:
        return HttpResponseRedirect(reverse('register'))

    #对密码进行sha256
    password = sha_256(password)

    user = User.objects.create(username=username, phone=phone, password=password, email=email, name=username)
    user.save()
    return JsonResponse({"msg": "success"})


@require_http_methods(['POST'])
def login_action(request):
    #TODO(koushushin):login
    username = request.POST.get("form-username")
    password = request.POST.get("form-password")

    if not all([username, password]):
        return HttpResponse("33333")

    password = sha_256(password)
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        logger.error("User havn't register in system")
        return HttpResponse("44444")

    res = user.vaild_user(username, password)
    if res:
        login(request, user)
        return JsonResponse({"msg": "success"})

    #用户名 密码不正确 或者用户已被禁用
    return redirect(reverse('main'))

@require_http_methods(['POST'])
def find_back(request):
    username = request.POST.get("form-username")
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        logger.error("User havn't register in system")
        return HttpResponse("44444")

    if not user.is_active:
        return JsonResponse({'msg': "user not authorized"})

    #TODO(koushushin): send email




def logout_action(request):
    try:
        logout(request)
    except Exception:
        pass
    return HttpResponseRedirect(reverse('main'))