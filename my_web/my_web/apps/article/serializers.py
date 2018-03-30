from rest_framework import serializers

from my_web.apps.article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_id','title','content','read_num','zan_num','tags','is_publish')
