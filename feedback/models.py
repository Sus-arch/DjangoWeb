import datetime

from django.db import models


class Feedback(models.Model):
    name = models.CharField('имя', max_length=150)
    text = models.TextField('текст')
    mail = models.EmailField('электронная почта')
    created_on = models.DateTimeField('время создания', default=datetime.datetime.now)
