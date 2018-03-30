from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer

from my_web.apps.tag.models import Tag
from my_web.apps.article.models import Article
from my_web.apps.tag.serializers import TagSerializer


from my_web.libs.Utils import Pagination

class TagList(APIView):

    def get(self, request, format=None):
        tags = Tag.objects.filter(is_publish=True)
        serializer= TagSerializer(tags, many=True)
        return Response(serializer.data)


class TagDetail(APIView):

    def get_object(self,pk):
        try:
            return Tag.objects.get(pk=pk)
        except:
            return Response(status.HTTP_404_NOT_FOUND)


    def get(self, request,pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


class ArticlesOfTag(generics.RetrieveAPIView):

    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        try:
            tag = Tag.objects.get(tag_id=self.request.query_params['tagId'])
        except:
            return Response(status.HTTP_404_NOT_FOUND)
        article = tag.article_set.all()

        tags = Tag.objects.all()

        template_name = "home.html"
        count = article.count()
        page = 1
        cur_page = 1
        page_count = 1
        start = (cur_page - 1) * page_count
        end = start + page_count
        pagination = Pagination.pagination(all_obj_counts=count, page_count=page_count, cur_page=cur_page)
        return Response(data={'articles': article, 'pagination': pagination, 'tags': tags}, template_name=template_name)

# def getTags(request,tag_id):
#     template_name = "home.html"
#     try:
#         tag = Tag.objects.get(tag_id=tag_id)
#         article = tag.article_set.all()
#         tags = Tag.objects.all()
#
        # count = article.count()
        # page = 1
        # cur_page = 1
        # page_count = 1
        # start = (cur_page - 1) * page_count
        # end = start + page_count
#     except:
#         raise Http404("Article does not exist")
#
#     pagination = Pagination.pagination(all_obj_counts=count, page_count=page_count, cur_page=cur_page)
#     return render(request, template_name, context={'articles':article,'pagination':pagination,'tags':tags})
