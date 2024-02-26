from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", related_name="profile", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        db_table = "Users"
    def __str__(self):
        return self.user.username


"""Ниже идут модели для Диграммы Гантта"""
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.IntegerField()
    is_disabled = models.BooleanField(default=True)
    duration = models.IntegerField(null=True)  # Duration in days
    completion = models.FloatField(null=True)  # Completion percentage
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
