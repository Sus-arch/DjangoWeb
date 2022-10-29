from django.db import models

from .validators import validate_amazing, validate_weight


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=200)
    weight = models.PositiveIntegerField(default=100,
                                         validators=[validate_weight])


class Tag(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=200)


class Item(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    text = models.TextField(validators=[validate_amazing])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
