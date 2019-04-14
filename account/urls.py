from . import views
from django.urls import path, include, re_path


urlpatterns = [
    path("main/", views.get_index, name="main"),
    path("SignUp/", views.get_register, name="register"),
    path("login/", views.login_action, name="login"),
    #path("test1/", views.accept_message),
    #path("test2/", views.get_model),
    path("register/", views.register)

    #path("SignUP/re")
]
