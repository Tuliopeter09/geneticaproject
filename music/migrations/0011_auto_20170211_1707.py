# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20170211_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
