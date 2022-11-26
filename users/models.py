from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField('день рождения', blank=True, null=True)

    def __str__(self):
        return f'День рождения пользователя {self.user}'

    class Meta:
        verbose_name = 'дополнительная информация'
        verbose_name_plural = 'дополнительная информация'
