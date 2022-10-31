from django.db import models

from .validators import validate_amazing, validate_weight
from core.models import MainInfo


class Category(MainInfo, models.Model):
    slug = models.SlugField('слаг', unique=True, max_length=200)
    weight = models.PositiveIntegerField('вес', default=100,
                                         validators=[validate_weight])

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(MainInfo):
    slug = models.SlugField('слаг', unique=True, max_length=200)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Item(MainInfo):
    text = models.TextField('описание', validators=[validate_amazing])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category',
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag, related_name='tags',
                                  verbose_name='теги')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
