from venv import logger

from django.db import models


# Create your models here.



class UserProfile(models.Model):
    user_id = models.IntegerField(verbose_name="идентификатор", null=True)
    email = models.EmailField(verbose_name="электронная почта", max_length=200)
    first_name = models.CharField(verbose_name="first_name", max_length=500)
    last_name = models.CharField(verbose_name="last_name", max_length=500)
    avatar = models.URLField(verbose_name="avatar", max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

class UserSupport(models.Model):
    user_profile = models.ManyToManyField(UserProfile, related_name='user_supports')
    url = models.URLField(verbose_name="url", max_length=200)
    text = models.CharField(verbose_name="text", max_length=500)

    class Meta:
        verbose_name = "Поддержка"
        verbose_name_plural = verbose_name



