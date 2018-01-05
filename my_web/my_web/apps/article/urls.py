from django.conf.urls import url,include,re_path

from my_web.apps.article.views import articleListView

urlpatterns = [
    url(r'^article/$',articleListView),
    re_path(r'^article?page=<int:page>/$',articleListView),
    re_path(r'^article?page=<int:page>&tag=<str:tag>/$',articleListView),
]