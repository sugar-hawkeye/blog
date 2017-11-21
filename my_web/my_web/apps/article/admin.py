from django.contrib import admin

from my_web.apps.article.models import Article
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','tag_name','read_num','is_publish')
    filter_horizontal = ('tags',)


admin.site.register(Article, ArticleAdmin)
