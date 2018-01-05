from django.conf.urls import url,include,re_path

from my_web.apps.tag.views import getTags

urlpatterns = [
    url(r'^tags/$',getTags),
]