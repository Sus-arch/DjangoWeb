from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField('день рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'дополнительная информация'
        verbose_name_plural = 'дополнительная информация'
