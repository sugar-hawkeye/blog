# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 06:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('tag_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=15, unique=True, verbose_name='标签名')),
                ('priority', models.IntegerField(verbose_name='排列顺序')),
                ('is_publish', models.BooleanField(default=False, verbose_name='是否发布')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag',
                'ordering': ['created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]