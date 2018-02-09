from django.urls import path

from my_web.apps.article.views import articleListView,articleDetailView,searchView

urlpatterns = [
    path(r'',articleListView),
    # path(r'/?page=<int:page>/$',articleListView),
    path(r'search/',searchView),
    path(r'page=<int:page>&tag=<str:tag>/',articleListView),
    path(r'article_id=<uuid:articleId>',articleDetailView),

]