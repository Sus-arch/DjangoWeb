# Generated by Django 3.2.4 on 2022-11-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='mail',
        ),
    ]
