from django.shortcuts import render
from django.http import Http404,HttpResponse

from my_web.apps.tag.models import Tag
# Create your views here.
from my_web.libs.Utils import Pagination


def getTags(request,tag_id):
    template_name = "home.html"
    try:
        tag = Tag.objects.get(tag_id=tag_id)
        article = tag.article_set.all()
        tags = Tag.objects.all()

        count = article.count()
        page = 1
        cur_page = 1
        page_count = 1
        start = (cur_page - 1) * page_count
        end = start + page_count
    except:
        raise Http404("Article does not exist")

    pagination = Pagination.pagination(all_obj_counts=count, page_count=page_count, cur_page=cur_page)
    return render(request, template_name, context={'articles':article,'pagination':pagination,'tags':tags})
