# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Image',
            field=models.ImageField(upload_to='/home/deependra/pothole-server/media/images', verbose_name='Image'),
        ),
    ]
