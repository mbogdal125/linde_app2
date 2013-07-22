from django.views.generic import TemplateView
from django.forms.formsets import BaseFormSet
from django.forms import ModelForm
from linde_app2.models import StockSheet, StockItem
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from insert_stocksheet.forms import testform
from django.forms.formsets import formset_factory

class TestForm(ModelForm):
    class Meta:
        model = StockItem
        fields = ['amount_real']

class InsertForm():
    def __init__(self, i):
        self.form = TestForm(instance = i)
        self.name = i.id_gas_cylinder_type.description

class InsertDataView(TemplateView):
    model = StockSheet
    template_name = "insert_stocksheet/insertdata.html"
    
    def get_context_data(self, **kwargs):
        context = super(InsertDataView, self).get_context_data(**kwargs)
        test = StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
        context['items'] = [] 
        for i in test:
            cur_form = InsertForm(i)
            context['items'].append(cur_form)
        return context
