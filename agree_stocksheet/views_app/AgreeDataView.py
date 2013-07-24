from django.views.generic import TemplateView
from django.forms.formsets import BaseFormSet
from django.forms import ModelForm
from linde_app2.models import StockSheet, StockItem, Stocktaking
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.formsets import formset_factory

class InsertForm():
    def __init__(self, i):
        self.form = TestForm(instance = i)
        self.name = i.id_gas_cylinder_type.description

class AgreeDataView(TemplateView):
    model = StockSheet
    template_name = "agree_stocksheet/agreedata.html"
    
    def get_context_data(self, **kwargs):
        context = super(AgreeDataView, self).get_context_data(**kwargs)
        if "stocksheet_number" in kwargs:
            context['stocksheet_number'] = kwargs['stocksheet_number']
        context['items'] =  StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
        context['notes'] =  StockSheet.objects.get(stock_sheet_number=kwargs['stocksheet_number']).notes
        return context

    def post(self, request, **kwargs):
        response = ""
        post = request._get_post()
        stocksheet = StockSheet.objects.get(stock_sheet_number=kwargs['stocksheet_number'])
        if "stocksheet_number" in kwargs:
            items = StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
            for i in items:
                StockItem.objects.filter(id = i.id).update(amount_real_agreed = post[str(i.id)])
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(status=3)
            if "notes" in post:
                StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(notes=post["notes"])
        return redirect('agree-chose-stocksheet', stocksheet.id_stocktaking.stocktaking_number)
