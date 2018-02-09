# -*- coding: utf-8 -*-

import uuid
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)

    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=15, verbose_name='标签名',unique=True)
    priority = models.IntegerField(verbose_name="排列顺序")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")


    def get_absolute_url(self):
        from my_web.apps.tag.views import  getTags
        return reverse(getTags,args=[self.tag_id])

    class Meta:
        db_table="tag"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '标签'
        verbose_name_plural = '标签'
        permissions = (
            ("tag_publish", "Can Publish Tag"),
            ("tag_delete", "Can Delete Tag"),
        )

    def __str__(self):
        return self.title