from django.db import models


class MainInfo(models.Model):
    name = models.CharField('Название', max_length=150)
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
