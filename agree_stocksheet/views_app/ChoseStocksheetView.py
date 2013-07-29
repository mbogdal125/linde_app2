#-*- coding: utf-8 -*
from django.views.generic import ListView
from linde_app2.models import StockSheet, StockSheetStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator

class ChoseStocksheetView(ListView):
    template_name = "chosestocksheet.html"
    model = StockSheet
    action = "agree-stocksheetdata"
    page_action = "agree-chose-stocksheet"

    def get_context_data(self, **kwargs):
        context = super(ChoseStocksheetView, self).get_context_data(**kwargs)
        context['action'] = self.action
        context['page'] = self.page
        context['page_action'] = self.page_action
        if 'stocktaking_number' in self.kwargs:
            context['stocktaking_number'] = int(self.kwargs['stocktaking_number'])
        return context

    def  get_queryset(self):
        p = Paginator(StockSheet.objects.order_by('-stock_sheet_number').filter(id_stocktaking__stocktaking_number=self.kwargs['stocktaking_number'],status__lte=3, status__gte=2), 15)
        if 'numpage' in self.kwargs:
            self.page = p.page(self.kwargs['numpage'])
        else:
            self.page = p.page(1)
        return self.page.object_list
