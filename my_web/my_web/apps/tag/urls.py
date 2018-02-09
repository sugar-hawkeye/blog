from django.urls import path

from my_web.apps.tag.views import getTags

urlpatterns = [
    path(r'tag_id=<uuid:tag_id>/',getTags),
]