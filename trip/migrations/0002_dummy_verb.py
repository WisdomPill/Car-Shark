# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='verb',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]