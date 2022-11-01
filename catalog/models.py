import re

from django.db import models
from django.db.models.signals import pre_save
from .validators import validate_weight, validate_amazing
from core.models import MainInfo
from django.core.exceptions import ValidationError


class Category(MainInfo):
    slug = models.SlugField('слаг', unique=True, max_length=200)
    weight = models.PositiveIntegerField('вес', default=100,
                                         validators=[validate_weight])
    canonical_name = models.CharField('каноническое название', max_length=150, unique=True, editable=False)

    def clean(self):
        can_name = re.sub(r'[^\s\w]', '', self.name.lower())
        if Category.objects.filter(canonical_name=can_name).count() != 0 and \
                Category.objects.filter(canonical_name=can_name).first().id != self.id:
            raise ValidationError('Данная категория уже есть')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(MainInfo):
    slug = models.SlugField('слаг', unique=True, max_length=200)
    canonical_name = models.CharField('каноническое название', max_length=150, unique=True, editable=False)

    def clean(self):
        can_name = re.sub(r'[^\s\w]', '', self.name.lower())
        if Tag.objects.filter(canonical_name=can_name).count() != 0:
            raise ValidationError(f'Данный тег уже есть')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Item(MainInfo):
    text = models.TextField('описание',
                            validators=[validate_amazing])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category',
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag, related_name='tags',
                                  verbose_name='теги')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


def catalog_pre_save(sender, instance, *args, **kwargs):
    instance.canonical_name = re.sub(r'[^\s\w]', '', instance.name.lower())


pre_save.connect(catalog_pre_save, sender=Category)


def tag_pre_save(sender, instance, *args, **kwargs):
    instance.canonical_name = re.sub(r'[^\s\w]', '', instance.name.lower())


pre_save.connect(catalog_pre_save, sender=Tag)
