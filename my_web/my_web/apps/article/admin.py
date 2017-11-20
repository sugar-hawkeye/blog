from django.contrib import admin

from my_web.apps.article.models import Article, ArticleBody

class ArticleAdmin(admin.ModelAdmin):
    pass


class ArticleBodyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleBody, ArticleBodyAdmin)