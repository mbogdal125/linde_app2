from django.http import Http404
from django.views.generic import TemplateView
from django.forms.formsets import BaseFormSet
from django.forms import ModelForm
from django.contrib.auth.models import User
from linde_app2.models import StockSheet, StockItem, Stocktaking, StocktakingStatus, AgreeOperation
from django.shortcuts import render, redirect, get_object_or_404
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
            stocksheet = StockSheet.objects.get(stock_sheet_number = kwargs['stocksheet_number'])
            if stocksheet.status.id not in {2,3}:
                raise Http404
            return context
        return redirect("home")

    def post(self, request, **kwargs):
        response = ""
        post = request._get_post()
        stocksheet = StockSheet.objects.get(stock_sheet_number=kwargs['stocksheet_number'])
        gen_info = AgreeOperation()
        gen_info.operator = get_object_or_404(User, id=self.request.user.id)
        gen_info.sheet_id = stocksheet
        gen_info.save()

        if "stocksheet_number" in kwargs:
            if stocksheet.status.id not in {2,3}:
                raise Http404
            items = StockItem.objects.filter(id_stock_sheet__stock_sheet_number = kwargs['stocksheet_number'])
            for i in items:
                StockItem.objects.filter(id = i.id).update(amount_real_agreed = post[str(i.id)])
            StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(status=3)
            if "notes" in post:
                StockSheet.objects.filter(stock_sheet_number=kwargs['stocksheet_number']).update(notes=post["notes"])
            #if its last one we will change stocktaking status to inserted
        if StockSheet.objects.filter(id_stocktaking__stocktaking_number=stocksheet.id_stocktaking.stocktaking_number, status=2):
            return redirect('agree-chose-stocksheet', stocksheet.id_stocktaking.stocktaking_number)
        stocksheet.id_stocktaking.status=StocktakingStatus.objects.get(id=3)
        stocksheet.id_stocktaking.save()
        return redirect('agree-chose-stocktaking')
