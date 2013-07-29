#*- coding: utf-8 -*
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.forms.formsets import BaseFormSet
from django.forms import ModelForm
from linde_app2.models import StockSheet, StockItem, Stocktaking, StocktakingStatus, InsertOperation, GasCylinderType
from django.shortcuts import render, redirect, get_object_or_404
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
            context['items']= GasCylinderType.objects.all()
            stocksheet = StockSheet.objects.get(stock_sheet_number = kwargs['stocksheet_number'])
            for i in context['items']:
                if StockItem.objects.filter(id_stock_sheet=stocksheet, id_gas_cylinder_type=i):
                    i.amount_real = StockItem.objects.get(id_stock_sheet=stocksheet, id_gas_cylinder_type=i).amount_real
            if stocksheet.status.id > 2:
                raise Http404
            return context
        return redirect('home')

    def post(self, request, **kwargs):
        response = ""
        post = request._get_post()
        if "stocksheet_number" in kwargs:
            stocksheet = StockSheet.objects.get(stock_sheet_number=kwargs['stocksheet_number'])
            gen_info = InsertOperation()
            gen_info.operator = get_object_or_404(User, id=self.request.user.id)
            gen_info.sheet_id = stocksheet
            gen_info.save()
            if stocksheet.status.id > 2:
                raise Http404
            items = GasCylinderType.objects.all()
            for i in items:
                if (isinstance(post[str(i.id)],int)) and (post[str(i.id)] != 0):
                    if StockItem.objects.filter(id_stock_sheet=stocksheet, id_gas_cylinder_type=i):
                        StockItem.objects.filter(id_stock_sheet=stocksheet, id_gas_cylinder_type=i).update(amount_real=post[str(i.id)])
                        StockItem.objects.filter(id_stock_sheet=stocksheet, id_gas_cylinder_type=i).update(amount_real_agreed=post[str(i.id)])
                    else:
                        cur_item = StockItem()
                        cur_item.id_gas_cylinder_type = i
                        cur_item.id_stock_sheet = stocksheet
                        cur_item.amount_real = post[str(i.id)]
                        cur_item.amount_real_agreed = post[str(i.id)]
                        cur_item.save()
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(status=2)
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(stockTakingDate=datetime.now())
        #if its last one we will change stocktaking status to inserted
        if StockSheet.objects.filter(id_stocktaking__stocktaking_number=stocksheet.id_stocktaking.stocktaking_number, status=1):
            return redirect('chose-stocksheet', stocksheet.id_stocktaking.stocktaking_number)
        stocksheet.id_stocktaking.status=StocktakingStatus.objects.get(id=2)
        stocksheet.id_stocktaking.save()
        return redirect('chose-stocktaking')

