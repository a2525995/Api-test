from . import views
from django.urls import path, include, re_path


urlpatterns = [
    path("", views.LoginView.as_view(), name="main"),
    path("sign_up/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.logout_action, name="logout"),
    #path("register/", views.register),

    #path("SignUP/re")
]
