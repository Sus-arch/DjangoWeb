from django.db import models


class MainInfo(models.Model):
    name = models.CharField('название', max_length=150)
    is_published = models.BooleanField('опубликовано', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
