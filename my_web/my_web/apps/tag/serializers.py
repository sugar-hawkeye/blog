from rest_framework import serializers

from my_web.apps.tag.models import Tag


class TagSerializer(serializers.ModelSerializer):


    class Meta:
        model = Tag
        fields = ('tag_id','title','priority','is_publish')
