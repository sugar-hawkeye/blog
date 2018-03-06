
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import render,  get_object_or_404

from my_web.apps.article.models import Article
from my_web.apps.tag.models import Tag
from my_web.libs.Utils import Pagination,read_md


def articleListView(request,page=1,tag=None):
    template_name = "home.html"
    tags = None
    try:
        cur_page = int(request.GET.get('page',1))
        tag = request.GET.get('tag',None)
        tags = Tag.objects.all()
    except ValueError:
        cur_page = 1
    if cur_page < 1:
        cur_page = 1
    page_count = 3
    start = (cur_page - 1) * page_count
    end = start + page_count
    try:
        if tag:
            objects = Article.objects.filter(tags=tag)[start:end]
            count = Article.objects.filter(tags=tag).count()
        else:
            objects = Article.objects.all()[start:end]
            count = Article.objects.count()
    except:
        raise Http404("Article does not exist")
    pagination = Pagination.pagination(all_obj_counts=count,page_count=page_count,cur_page=cur_page)
    return render(request,template_name,context={'articles':objects,'pagination':pagination,'tags':tags})


def articleDetailView(request,articleId):
    template_name = "detail.html"
    obj = get_object_or_404(Article,article_id=articleId)
    obj.content = read_md(obj.content)
    tags = Tag.objects.all()
    return render(request,template_name,context={'article':obj,'tags':tags,'markdown':obj.content})

def searchView(request,page=1):
    template_name = "home.html"

    tags = None
    try:
        title = request.GET.get('title', '')
        cur_page = int(request.GET.get('page',1))
        tags = Tag.objects.all()
    except ValueError:
        cur_page = 1
    if cur_page < 1:
        cur_page = 1
    page_count = 1
    start = (cur_page - 1) * page_count
    end = start + page_count
    try:
        objects = Article.objects.filter(title__contains=title)[start:end]
        count = objects.count()

    except:
        raise Http404("Article does not exist")
    pagination = Pagination.pagination(all_obj_counts=count,page_count=page_count,cur_page=cur_page)
    return render(request,template_name,context={'articles':objects,'pagination':pagination,'tags':tags})


def getTag(request):
    template_name = "home.html"
