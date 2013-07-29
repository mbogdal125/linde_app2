#-*- coding: utf-8 -*
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from linde_app2.models import Stocktaking, StocktakingStatus, StocktakingType, Customer, StockSheet, StockSheetStatus, StockItem, GasCylinderType, GenerateStockTaking
from django.shortcuts import render, redirect, get_object_or_404
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
        gen_info = GenerateStockTaking()
        gen_info.stock_taking = Staking
        gen_info.operator = get_object_or_404(User, id=self.request.user.id)
        gen_info.save()
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


        return redirect('home')
