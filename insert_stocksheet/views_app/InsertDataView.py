from django.views.generic import TemplateView
from django.forms.formsets import BaseFormSet
from django.forms import ModelForm
from linde_app2.models import StockSheet, StockItem, Stocktaking
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.formsets import formset_factory
from datetime import datetime

class InsertForm():
    def __init__(self, i):
        self.form = TestForm(instance = i)
        self.name = i.id_gas_cylinder_type.description

class InsertDataView(TemplateView):
    model = StockSheet
    template_name = "insert_stocksheet/insertdata.html"
    
    def get_context_data(self, **kwargs):
        context = super(InsertDataView, self).get_context_data(**kwargs)
        if "stocksheet_number" in kwargs:
            context['stocksheet_number'] = kwargs['stocksheet_number']
        context['items'] =  StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
        return context

    def post(self, request, **kwargs):
        response = ""
        post = request._get_post()
        stocksheet = StockSheet.objects.get(stock_sheet_number=kwargs['stocksheet_number'])
        if "stocksheet_number" in kwargs:
            items = StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
            for i in items:
                StockItem.objects.filter(id = i.id).update(amount_real = post[str(i.id)])
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(status=2)
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(stockTakingDate=datetime.now())
        return redirect('chose-stocksheet', stocksheet.id_stocktaking.stocktaking_number)
