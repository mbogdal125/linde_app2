from django.views.generic import ListView
from django.views.generic.edit import CreateView
from linde_app2.models import Customer
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

class Customers(ListView):
    template_name = "manage_data/customers.html"
    model = Customer 

class AddCustomer(CreateView):
    model = Customer

