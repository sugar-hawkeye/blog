# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20171121_0600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'permissions': (('channel_publish', 'Can Publish Article'),), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='文章标题'),
        ),
    ]
