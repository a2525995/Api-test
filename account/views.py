from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from public.utils import *
from .models import User
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.views.generic import TemplateView
# Create your views here.

logger = logging.getLogger(__file__)

class LoginView(View):
    def get(self, request):
        return render(request, 'account/index.html')

    def post(self, request):
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

        # 用户名 密码不正确 或者用户已被禁用
        return redirect(reverse('main'))

class RegisterView(View):
    def get(self, request):
        return render(request, 'account/register.html')

    def post(self, request):
        username = request.POST.get('form-username')
        password = request.POST.get('form-password')
        email = request.POST.get('form-email')
        phone = request.POST.get('form-phone')

        # 如果任意一项为空，则返回注册页面
        if not all([username, password, email, phone]):
            return HttpResponseRedirect(reverse('main'))

        # 如果邮箱不符合正则表达式，返回注册页面
        if not check_email(email):
            return HttpResponseRedirect(reverse('main'))

        if not check_phone(phone):
            return HttpResponseRedirect(reverse('main'))

        user_email = User.objects.filter(email__exact=email)
        if user_email:
            return HttpResponseRedirect(reverse('register'))

        user_phone = User.objects.filter(phone__exact=phone)
        if user_phone:
            return HttpResponseRedirect(reverse('register'))

        user = User.objects.filter(username__exact=username)
        if user:
            return HttpResponseRedirect(reverse('register'))

        password = sha_256(password)

        user = User.objects.create(username=username, phone=phone, password=password, email=email, name=username)
        user.save()
        return JsonResponse({"msg": "success"})

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