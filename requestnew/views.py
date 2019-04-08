from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import auth
from requestnew.models import *
import logging
from public.utils import check_email, check_phone, sha_256
# Create your views here.

log = logging.getLogger("requestnew")

def get_index(request):
    return render(request, 'index.html')

def get_register(request):
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        #TODO(koushushin):login
        pass
    return redirect('main')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('form-username')
        password = request.POST.get('form-password')
        email = request.POST.get('form-email')
        phone = request.POST.get('form-phone')

        #如果任意一项为空，则返回注册页面
        if not all([username, password, email, phone]):
            return get_register(request)

        #如果邮箱不符合正则表达式，返回注册页面
        if not check_email(email):
            return get_register(request)

        # 如果手机不符合正则表达式，返回注册页面
        if not check_phone(phone):
            return get_register(request)

        #检测邮箱
        user_email = UserInfo.objects.filter(email__exact=email)
        if user_email:
            return render(request, 'register.html')

        #检测手机
        user_phone = UserInfo.objects.filter(phone__exact=phone)
        if user_phone:
            return render(request, 'register.html')

        #检测用户名
        user = UserInfo.objects.filter(username__exact=username)
        if user:
            return render(request, 'register.html')

        #对密码进行sha256
        password = sha_256(password)

        user = UserInfo.objects.create(username=username, phone=phone, password=password, email=email)
        user.save()
        #TODO(koushushin):返回登录之后的页面
        pass
    return redirect('register')

def accept_message(request):
    data = {
        "msg": "ok",
        "result": "1"
    }
    log.info("123")
    return JsonResponse(data, status=200)


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            UserInfo.objects.create(username=username, password=password)
    return None


#
def get_model(request):
    obj = UserInfo.objects.all().values()

    print(obj)
    obj = list(obj)
    print(type(obj[1]))
    d = {
        "test": obj
    }
    return JsonResponse(data=d, safe=False)


