# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-20 07:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('read_num', models.PositiveIntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\x95\xb0')),
                ('is_publish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\xba')),
                ('tag', models.ManyToManyField(null=True, to='tag.Tag', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'ordering': ['created_at'],
                'db_table': 'article',
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
                'get_latest_by': 'created_at',
            },
        ),
    ]
