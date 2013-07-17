from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import Stocktaking, StocktakingStatus, StocktakingType
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
        return redirect('home')
