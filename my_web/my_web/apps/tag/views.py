from django.shortcuts import render
from django.http import Http404,HttpResponse

from my_web.apps.tag.models import Tag
# Create your views here.
def getTags(request):
    try:
        objects = Tag.objects.all()
    except:
        raise Http404("Article does not exist")
    return HttpResponse({'tags':object})