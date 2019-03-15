# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Course(models.Model):
    cid = models.CharField(db_column='CId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cname = models.CharField(db_column='Cname', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TId', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Sc(models.Model):
    sid = models.CharField(db_column='SId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(max_digits=18, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SC'


class Student(models.Model):
    sid = models.CharField(db_column='SId', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sage = models.DateTimeField(db_column='Sage', blank=True, null=True)  # Field name made lowercase.
    ssex = models.CharField(db_column='Ssex', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'


class Teacher(models.Model):
    tid = models.CharField(db_column='TId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tname = models.CharField(db_column='Tname', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teacher'


class Courses(models.Model):
    student = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'courses'
