# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from my_web.apps.tag.models import Tag



class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)

    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='文章标题',unique=True)
    content = models.TextField(verbose_name='文章内容',null=True,blank=True)

    read_num = models.PositiveIntegerField(default=0,verbose_name='阅读数')
    zan_num = models.PositiveIntegerField(default=0, verbose_name='点赞数')

    tags = models.ManyToManyField(Tag, verbose_name="所属标签")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from my_web.apps.article.views import  articleDetailView
        return reverse(articleDetailView,args=[self.article_id])



    def tag_name(self):
        # tag = Tag.objects.filter(article__title__exact=self.title)
        article = Article.objects.get(article_id=self.article_id)
        tags = article.tags.all()
        list = []
        if tags:
            for tag in tags:
                list.append(tag.title)
            return ' , '.join(list)
        else:
            return None
    tag_name.short_description = "所属标签"
    tag_name.empty_value_display = '----'


    class Meta:
        db_table="article"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '文章'
        verbose_name_plural = '文章'
        permissions = (
            ("article_publish", "Can Publish Article"),
            ("aritcle_delete", "Can Delete Article"),
        )


