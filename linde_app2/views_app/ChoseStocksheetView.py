#-*- coding: utf-8 -*
from django.views.generic import ListView
from linde_app2.models import StockSheet, StockSheetStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class ChoseStocksheetView(ListView):
    template_name = "chosestocksheet.html"
    model = StockSheet
    action = "insert-stocksheetdata"

    def get_context_data(self, **kwargs):
        context = super(ChoseStocksheetView, self).get_context_data(**kwargs)
        context['action'] = self.action
        return context

    def get_queryset(self):
        queryset = StockSheet.objects.order_by('-stock_sheet_number').filter(id_stocktaking__stocktaking_number=self.kwargs['stocktaking_number'],status__lte=2).prefetch_related('id_customer', 'status')
        return queryset
