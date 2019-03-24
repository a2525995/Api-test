from . import views
from django.urls import path, include, re_path


urlpatterns = [
    path("test/", views.login),
    path("test1/", views.accept_message),
    path("test2/", views.get_model)
]
