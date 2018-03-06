from django.contrib import admin

from my_web.apps.article.models import Article
from django.db import models


from .forms import ArticleForm
from my_web.libs.Utils import save_md,read_md

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','tag_name','read_num','is_publish')
    filter_horizontal = ('tags',)
    form = ArticleForm

    article = None

    view_on_site = True

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if not self.article or obj.article_id != self.article.article_id:
                self.article = self.get_object(request, obj.article_id)
            obj.content = self.article.content
            content = read_md(obj.content)
            obj.content = content

        return super(ArticleAdmin,self).get_form(request, obj, **kwargs)


    def save_form(self, request, form, change):
        obj = super(ArticleAdmin, self).save_form(request, form, change)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            tag = list(tags)[0]
            content = form.cleaned_data['content']
            title = form.cleaned_data['title']
            path = save_md(content, title, tag)
            obj.content = path
        return obj



    def save_model(self, request, obj, form, change):
        super(ArticleAdmin, self).save_model(request, obj,form, change)

admin.site.register(Article, ArticleAdmin)
