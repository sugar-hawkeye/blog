from django.urls import re_path

from my_web.apps.article.models import Article
from my_web.apps.article.serializers import ArticleSerializer
from my_web.apps.article.views import ArticleList,ArticleDetail,api_root
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^', ArticleList.as_view(), name='article-list'),
    re_path(r'^article/$', ArticleList.as_view(), name='article-list'),
    # re_path(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view(), name='article-detail'),
    # re_path(r'^$',api_root),
]
urlpatterns = format_suffix_patterns(urlpatterns)

# from my_web.apps.article.views import articleListView,articleDetailView,searchView
#
# urlpatterns = [
#     # path(r'',articleListView),
#     # # path(r'/?page=<int:page>/$',articleListView),
#     # path(r'search/',searchView),
#     # path(r'page=<int:page>&tag=<str:tag>/',articleListView),
#     # path(r'article_id=<uuid:articleId>',articleDetailView),
#
# ]

