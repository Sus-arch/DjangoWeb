# Generated by Django 3.2 on 2022-10-29 15:26

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('weight', models.PositiveIntegerField(default=100, validators=[catalog.validators.validate_weight])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('text', models.TextField(validators=[catalog.validators.validate_amazing])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('tags', models.ManyToManyField(to='catalog.Tag')),
            ],
        ),
    ]
