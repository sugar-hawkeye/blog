
from django.http import Http404
from django.http import HttpResponseBadRequest

from django.shortcuts import render

from django.views.generic.base import TemplateView
from my_web.apps.article.models import Article



class ArticleListView(TemplateView):
    template_name = "home.html"
    http_method_names = ['get','head']

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)


        if not request.GET['page']:
            page = 1
        page = request.GET['page']
        if page.isdigit():
            page = int(page)
            if page < 1:
                page = 1
            page_count = 1
            start = (page - 1)*page_count
            end = start+page_count
            try:
                objects = Article.objects.all()[start:end]
                context['articles'] = objects

            except objects.DoesNotExit:
                raise Http404("Article does not exist")
        else:
            return HttpResponseBadRequest(request)
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)


        return context