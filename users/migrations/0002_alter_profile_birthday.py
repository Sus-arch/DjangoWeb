# Generated by Django 3.2.4 on 2022-11-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='день рождения'),
        ),
    ]
