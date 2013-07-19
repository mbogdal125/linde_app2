from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import Customer
from manage_data.forms import AddCustomerForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

class Customers(ListView):
    template_name = "manage_data/customers.html"
    model = Customer 

class AddCustomer(FormView):
    form_class = AddCustomerForm
    template_name = "manage_data/add_customer.html"

    def form_valid(self, form):
        Cust = Customer()
        if Customer.objects.count() == None:
            Cust.customer_number = 0
        else:
            Cust.customer_number = Customer.objects.count()
        Cust.name = form.cleaned_data['name']
        Cust.address = form.cleaned_data['address']
        Cust.address2 = form.cleaned_data['address2']
        Cust.phone = form.cleaned_data['phone']
        Cust.nip = form.cleaned_data['nip']
        Cust.headquaters = form.cleaned_data['headquaters']
        Cust.active = True
        Cust.save()
        return redirect("list-customers")
