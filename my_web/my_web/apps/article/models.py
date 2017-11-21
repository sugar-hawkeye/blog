# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from my_web.apps.tag.models import Tag



class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)
    title = models.CharField(max_length=50, verbose_name='文章标题',unique=True)
    path_article = models.CharField(verbose_name='文章地址',max_length=255,default='')
    content = models.TextField(verbose_name='文章内容',null=True,blank=True)

    read_num = models.PositiveIntegerField(default=0,verbose_name='阅读数')
    zan_num = models.PositiveIntegerField(default=0, verbose_name='点赞数')

    tags = models.ManyToManyField(Tag, verbose_name="所属标签",null=True,blank=True)
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('article', args=[str(self.id)])


    def tag_name(self):
        # tags = Tag.objects.filter(article__title__exact=self.title)
        article = Article.objects.get(id=1)
        print('tags === %s' % article.tags.all())

        tag_string = ''
        for tag in article.tags.all():
            tag = tag.title+' , '
            tag_string += tag

        return None
    tag_name.short_description = "所属标签"
    tag_name.empty_value_display = '-- --'


    class Meta:
        db_table="article"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '文章'
        verbose_name_plural = '文章'
        permissions = (
            ("channel_publish", "Can Publish Article"),
        )


