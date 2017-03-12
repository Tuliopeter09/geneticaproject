# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user_logo', models.FileField(upload_to=b'')),
            ],
        ),
    ]
