# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_auto_20160303_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Status',
            field=models.CharField(default='a', max_length=1),
        ),
    ]
