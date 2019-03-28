# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):
    uid = models.AutoField(db_column='uid', max_length=10, primary_key=True, null=False ,unique=True)
    username = models.CharField(db_column='username', max_length=150, null=False, blank=False)
    password = models.CharField(db_column='password', max_length=150, null=False, blank=False)
    email = models.CharField(db_column='email', max_length=254, null=True, unique=True)
    name = models.CharField(db_column='name', max_length=150, null=True, blank=True)
    create_time = models.DateField(db_column='create_time', max_length=30, auto_now_add=True)
    last_login = models.DateTimeField(db_column='last_login', max_length=30, auto_now=True)
    phone = models.CharField(max_length=11, null=True, unique=True)

class Publish(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=63,null=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    color = models.CharField(max_length=64)
    page_num = models.IntegerField(null=True)
    publisher = models.ForeignKey("Publish",on_delete=models.CASCADE,null=True)  #一对多的关系。2.0django中，当有主外键和其他对应关系时，需要设置。
    author = models.ManyToManyField("Author")
    def __str__(self):
        return  self.title
