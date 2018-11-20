from django.db import models

# Create your models here.


class Classes(models.Model):
    """班级"""
    caption = models.CharField(max_length = 32)


class Student(models.Model):
    """学生"""
    name = models.CharField(max_length = 32)
    classes = models.ForeignKey('Classes', on_delete = 'CASCADE')


class Teacher(models.Model):
    """老师"""
    name = models.CharField(max_length = 32)
    classes = models.ManyToManyField('Classes')


class Administrator(models.Model):
    """管理员"""
    username = models.CharField(max_length = 32)
    password = models.IntegerField()
