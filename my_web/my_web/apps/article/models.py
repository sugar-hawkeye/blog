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


    read_num = models.PositiveIntegerField(default=0,verbose_name='阅读数')

    tag = models.ManyToManyField(Tag, verbose_name="所属标签",null=True)
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")

    def __unicode__(self):
        return self.title

    class Meta:
        db_table="article"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '文章'
        verbose_name_plural = '文章'

# 表的记录并不多，但是字段却很长，表占用空间很大，检索表的时候需要执行大量的IO，严重降低了性能。
# 这时需要把大的字段拆分到另一个表，并且该表与原表是一对一的关系。

class ArticleBody(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)

    content = models.TextField(verbose_name='文章内容')
    article = models.OneToOneField(Article, on_delete=models.CASCADE,verbose_name="所属文章")

    class Meta:
        db_table="article_body"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '文章内容'
        verbose_name_plural = '文章内容'