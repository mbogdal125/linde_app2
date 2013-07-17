from django.views.generic import ListView
from linde_app2.models import Stocktaking, StocktakingStatus, StocktakingType
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class HomeView(ListView):
    template_name = "index.html"
    model = Stocktaking
    scroll_size = 50

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        page_number = 0
        if 'page_number' in self.kwargs:
            page_number = int(self.kwargs['page_number'])
        maxpage = Stocktaking.objects.count() / self.scroll_size
        context['prev_page_num'] = page_number - 1
        context['next_page_num'] = page_number + 1
        context['maxpage'] = maxpage
        return context
    
    def get_queryset(self):
        page_number = 0
        limit = 0
        if 'page_number' in self.kwargs:
            page_number = int(self.kwargs['page_number'])
        offset = page_number * self.scroll_size
        queryset = Stocktaking.objects.order_by('-stocktaking_number').prefetch_related('type', 'status')[offset:offset + self.scroll_size]
        return queryset