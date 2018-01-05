from django.http import Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from my_web.apps.article.models import Article
from my_web.libs.Utils import Pagination

def articleListView(request,page=1,tag=None):
    template_name = "home.html"
    try:
        cur_page = int(request.GET.get('page',1))
        tag = request.GET.get('tag',None)
    except ValueError:
        cur_page = 1
    if cur_page < 1:
        cur_page = 1
    page_count = 1
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
    return render(request,template_name,context={'articles':objects,'pagination':pagination})




