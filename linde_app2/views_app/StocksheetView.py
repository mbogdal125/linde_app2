#-*- coding: utf-8 -*
from django.views.generic import ListView
from linde_app2.models import StockSheet, StockItem
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class StocksheetView(ListView):
    template_name = "stocksheet.html"
    model = StockItem

    def get_queryset(self):
        queryset = StockItem.objects.order_by('-id_stock_sheet').filter(id_stock_sheet__stock_sheet_number=self.kwargs['stocksheet_number'])
        return queryset
