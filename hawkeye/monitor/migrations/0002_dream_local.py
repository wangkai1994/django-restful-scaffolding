# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='local',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
