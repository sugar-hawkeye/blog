# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20171206_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='path_article',
        ),
    ]