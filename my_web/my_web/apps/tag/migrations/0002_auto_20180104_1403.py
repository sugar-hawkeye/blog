# Generated by Django 2.0 on 2018-01-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'permissions': (('tag_publish', 'Can Publish Tag'), ('tag_delete', 'Can Delete Tag')), 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
    ]
