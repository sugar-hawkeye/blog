from django.urls import re_path

from my_web.apps.tag.views import TagList,TagDetail,ArticlesOfTag
from my_web.apps.tag.serializers import TagSerializer

urlpatterns = [
    re_path(r'^tags/$', TagList.as_view(), name='tag-list'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name='tag-detail'),
    re_path(r'^tag/$',ArticlesOfTag.as_view(),name='tag-article-list'),
]


# urlpatterns = [
#     path(r'tag_id=<uuid:tag_id>/',getTags),
# ]