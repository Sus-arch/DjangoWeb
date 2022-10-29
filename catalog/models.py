from django.db import models

from .validators import validate_amazing, validate_weight
from core.models import MainInfo


class Category(MainInfo, models.Model):
    slug = models.SlugField('Слаг', unique=True, max_length=200)
    weight = models.PositiveIntegerField('Вес', default=100,
                                         validators=[validate_weight])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(MainInfo):
    slug = models.SlugField('Слаг', unique=True, max_length=200)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Item(MainInfo):
    text = models.TextField('Описание', validators=[validate_amazing])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category', name='Категория')
    tags = models.ManyToManyField(Tag, related_name='tags', name='Теги')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
