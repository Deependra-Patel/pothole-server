# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-18 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20160504_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Response',
            field=models.CharField(choices=[['y', 'Yes'], ['n', 'No'], ['m', 'Not Sure']], max_length=1),
        ),
    ]
