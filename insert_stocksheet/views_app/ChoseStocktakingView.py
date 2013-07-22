from django.views.generic import ListView
from linde_app2.models import Stocktaking, StocktakingStatus, StocktakingType
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class ChoseStocktakingView(ListView):
    template_name = "insert_stocksheet/chosestocktaking.html"
    model = Stocktaking
    scroll_size = 50
    action = "chose-stocksheet"

    def get_context_data(self, **kwargs):
        context = super(ChoseStocktakingView, self).get_context_data(**kwargs)
        page_number = 0
        if 'page_number' in self.kwargs:
            page_number = int(self.kwargs['page_number'])
        maxpage = Stocktaking.objects.count() / self.scroll_size 
        if Stocktaking.objects.count() % self.scroll_size != 0:
            maxpage += 1
        context['prev_page_num'] = page_number - 1
        context['next_page_num'] = page_number + 1
        context['maxpage'] = maxpage
        context['action'] = self.action
        return context
    
    def get_queryset(self):
        page_number = 0
        limit = 0
        if 'page_number' in self.kwargs:
            page_number = int(self.kwargs['page_number'])
        offset = page_number * self.scroll_size
        queryset = Stocktaking.objects.order_by('-stocktaking_number').prefetch_related('type', 'status')[offset:offset + self.scroll_size]
        return queryset
