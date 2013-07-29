#-*- coding: utf-8 -*
from django.views.generic import ListView
from linde_app2.models import StockSheet, StockSheetStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class StocktakingView(ListView):
    template_name = "stocktaking.html"
    model = StockSheet

    def get_queryset(self):
        queryset = StockSheet.objects.order_by('-stock_sheet_number').filter(id_stocktaking__stocktaking_number=self.kwargs['stocktaking_number']).prefetch_related('id_customer', 'status')
        return queryset
