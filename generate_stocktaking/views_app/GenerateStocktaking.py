from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import Stocktaking, StocktakingStatus, StocktakingType, Customer, StockSheet, StockSheetStatus, StockItem, GasCylinderType
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from generate_stocktaking.forms import GenStocktakingForm

class GenerateStocktaking(FormView):
    form_class = GenStocktakingForm
    template_name = "generate_stocktaking/GenerateStocktaking.html"

    def form_valid(self, form):
        Staking = Stocktaking()
        if Stocktaking.objects.count() == None:
            Staking.stocktaking_number = 0
        else:
            Staking.stocktaking_number = Stocktaking.objects.count()
        Staking.date = form.cleaned_data['date']
        Staking.type = form.cleaned_data['type']
        Staking.status_id = 1
        Staking.active = True
        Staking.save()
        for cur_cust in Customer.objects.filter(active=True):
            new_sheet = StockSheet()
            if StockSheet.objects.count() == None:
                new_sheet.stock_sheet_number = 0
            else:
                new_sheet.stock_sheet_number = StockSheet.objects.count()
            new_sheet.stockTakingDate = Staking.date
            new_sheet.id_customer = cur_cust
            new_sheet.id_stocktaking = Staking
            new_sheet.status = StockSheetStatus(1)
            new_sheet.archival = False
            new_sheet.save()
            for cur_type in GasCylinderType.objects.all():
                new_item = StockItem()
                new_item.id_stock_sheet = new_sheet
                new_item.id_gas_cylinder_type = cur_type
                new_item.amount_real = 0
                new_item.amount_real_agreed = 0
                new_item.amount_sap_= 0
                new_item.amount_sap_agreed = 0
                new_item.save()


        return redirect('home')
