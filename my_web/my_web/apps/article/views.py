from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from my_web.apps.article.models import Article
from my_web.apps.tag.models import Tag
from my_web.apps.article.serializers import ArticleSerializer
from my_web.apps.tag.serializers import TagSerializer

from my_web.libs.Utils import Pagination,read_md

class ArticleList(APIView):
    renderer_classes = (TemplateHTMLRenderer)

    def get(self,request,format=None):
        cur_page = int(request.query_params.get('page',1))
        if cur_page < 1:
            cur_page = 1
        page_count = 2
        start = (cur_page - 1) * page_count
        end = start + page_count

        articles = Article.objects.filter(is_publish=True)[start:end]
        serializer = ArticleSerializer(articles, many=True)

        tags = Tag.objects.all()
        tagserializer = TagSerializer(tags, many=True)

        template_name = "home.html"
        count = Article.objects.filter(is_publish=True).count()

        pagination = Pagination.pagination(all_obj_counts=count, page_count=page_count, cur_page=cur_page)
        return Response(data={'articles': serializer.data, 'pagination': pagination, 'tags': tagserializer.data}, template_name=template_name)


class ArticleDetail(APIView):

    def get_object(self,pk):
        try:
            return Article.objects.get(pk=pk)
        except:
            return Response(status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = ArticleSerializer(tag)
        return Response(serializer.data)

from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-detail', args=[63413857364739072,]),
    })


# def articleListView(request,page=1,tag=None):
#     template_name = "home.html"
#     tags = None
#     try:
#         cur_page = int(request.GET.get('page',1))
#         tag = request.GET.get('tag',None)
#         tags = Tag.objects.all()
#     except ValueError:
#         cur_page = 1
#     if cur_page < 1:
#         cur_page = 1
#     page_count = 3
#     start = (cur_page - 1) * page_count
#     end = start + page_count
#     try:
#         if tag:
#             objects = Article.objects.filter(tags=tag)[start:end]
#             count = Article.objects.filter(tags=tag).count()
#         else:
#             objects = Article.objects.all()[start:end]
#             count = Article.objects.count()
#     except:
#         raise Http404("Article does not exist")
#     pagination = Pagination.pagination(all_obj_counts=count,page_count=page_count,cur_page=cur_page)
#     return render(request,template_name,context={'articles':objects,'pagination':pagination,'tags':tags})
#
#
# def articleDetailView(request,articleId):
#     template_name = "detail.html"
#     obj = get_object_or_404(Article,article_id=articleId)
#     obj.content = read_md(obj.content)
#     tags = Tag.objects.all()
#     return render(request,template_name,context={'article':obj,'tags':tags,'markdown':obj.content})
#
# def searchView(request,page=1):
#     template_name = "home.html"
#
#     tags = None
#     try:
#         title = request.GET.get('title', '')
#         cur_page = int(request.GET.get('page',1))
#         tags = Tag.objects.all()
#     except ValueError:
#         cur_page = 1
#     if cur_page < 1:
#         cur_page = 1
#     page_count = 1
#     start = (cur_page - 1) * page_count
#     end = start + page_count
#     try:
#         objects = Article.objects.filter(title__contains=title)[start:end]
#         count = objects.count()
#
#     except:
#         raise Http404("Article does not exist")
#     pagination = Pagination.pagination(all_obj_counts=count,page_count=page_count,cur_page=cur_page)
#     return render(request,template_name,context={'articles':objects,'pagination':pagination,'tags':tags})
#
#
# def getTag(request):
#     template_name = "home.html"
