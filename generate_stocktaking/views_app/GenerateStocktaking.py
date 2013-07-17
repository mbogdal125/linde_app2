from django.views.generic import ListView
from django.views.generic.edit import CreateView
from linde_app2.models import Stocktaking
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class GenerateStocktaking(CreateView):
    model = Stocktaking
    template_name = "generate_stocktaking/GenerateStocktaking.html"
