# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 05:39
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('City', models.CharField(max_length=3)),
                ('Fixed', models.BooleanField(default='False')),
                ('Reviewed', models.BooleanField(default='False')),
                ('Type', models.CharField(default='p', max_length=1)),
                ('Severity', models.IntegerField(blank=True, default=5)),
                ('PhotoPath', models.CharField(max_length=200)),
                ('Info', models.CharField(blank=True, max_length=300, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('ReporterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
