
from django.http import Http404
from django.http import HttpResponseBadRequest

from django.shortcuts import render

from my_web.apps.article.models import Article

def articleListView(request,page=1):
    template_name = "home.html"
    if page < 1:
        page = 1
    page_count = 1
    start = (page - 1) * page_count
    end = start + page_count
    try:
        objects = Article.objects.all()[start:end]
    except objects.DoesNotExit:
        raise Http404("Article does not exist")

    return render(request,template_name,context={'articles':objects})




