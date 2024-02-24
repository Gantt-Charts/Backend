from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", related_name="profile", on_delete=models.CASCADE)
