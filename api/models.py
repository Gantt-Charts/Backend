from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    class Meta:
        swappable = 'AUTH_USER_MODEL'


"""Ниже идут модели для Диграммы Гантта"""
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects',)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    start = models.DateField()
    end = models.DateField()
    progress = models.IntegerField()
    isDisabled = models.BooleanField(default=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
