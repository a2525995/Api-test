from django.db import models
from django.contrib.auth.models import AbstractUser
from public.utils import sha_256
# Create your models here.


class User(AbstractUser):
    uid = models.AutoField(db_column='uid', max_length=10, primary_key=True, null=False ,unique=True)
    username = models.CharField(db_column='username', max_length=150, null=False, blank=False, unique=True)
    password = models.CharField(db_column='password', max_length=150, null=False, blank=False)
    email = models.CharField(db_column='email', max_length=254, null=True, unique=True)
    name = models.CharField(db_column='name', max_length=150, null=True, blank=True)
    create_time = models.DateField(db_column='create_time', max_length=30, auto_now_add=True)
    last_login = models.DateTimeField(db_column='last_login', max_length=30, auto_now=True)
    phone = models.CharField(db_column='phone', max_length=11, null=True, unique=True)
    is_active = models.BooleanField(db_column='is_active', default=True)


    class Meta:
        verbose_name = '用户信息'
        db_table = "User"

    @classmethod
    def set_password(cls, password):
        cls.password = sha_256(password)
        return True

    @classmethod
    def set_email(cls, email):
        cls.email = email
        return True

    @classmethod
    def vaild_user(cls, username, password):
        user = cls.objects.get(username=username)
        return user.username == username and user.password == password and user.is_active is True

    @classmethod
    def delete_user(cls):
        cls.is_active = False
        return True
