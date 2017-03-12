# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0009_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_logo',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=b'', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.OneToOneField(default=b'', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'', max_length=250),
        ),
    ]
