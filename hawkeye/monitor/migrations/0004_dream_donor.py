# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='donor',
            field=models.ManyToManyField(blank=True, null=True, to='monitor.Donor'),
        ),
    ]
