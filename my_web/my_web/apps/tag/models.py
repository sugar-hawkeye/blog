# -*- coding: utf-8 -*-


from django.db import models

from django.contrib.auth.models import User



# Create your models here.
class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)
    title = models.CharField(max_length=15, verbose_name='标签名',unique=True)
    priority = models.IntegerField(verbose_name="排列顺序")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")


    def __unicode__(self):
        return self.title

    class Meta:
        db_table="tag"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '标签'
        verbose_name_plural = '标签'
