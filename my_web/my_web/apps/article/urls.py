from django.conf.urls import url,include,re_path

from my_web.apps.article.views import ArticleListView

urlpatterns = [
    url(r'^article/$',ArticleListView.as_view()),
    re_path(r'^article?(?:page=(?P<page_number>\d+)/)?$',ArticleListView.as_view(),name='articles'),
]