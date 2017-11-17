# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from my_web.apps.tag.models import Tag

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')

    read_num = models.PositiveIntegerField(default=0,verbose_name='阅读数')

    tag_id = models.ManyToManyField(Tag, on_delete=models.SET_NULL, verbose_name="所属标签",null=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table="article"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '文章'
        verbose_name_plural = '文章'