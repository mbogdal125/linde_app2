#-*- coding: utf-8 -*
from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import Customer
from manage_data.forms import AddCustomerForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator

class Customers(ListView):
    template_name = "manage_data/customers.html"
    model = Customer

    def  get_queryset(self):
        p = Paginator(Customer.objects.all(), 15)
        if 'numpage' in self.kwargs:
            self.page = p.page(self.kwargs['numpage'])
        else:
            self.page = p.page(1)
        for i in self.page.object_list:
            print i.name
        return self.page.object_list

    def get_context_data(self, **kwargs):
        context = super(Customers, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context
    

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
        Cust.street = form.cleaned_data['street']
        Cust.city = form.cleaned_data['city']
        Cust.postalcode = form.cleaned_data['postalcode']
        Cust.flat_number = form.cleaned_data['flat_number']
        Cust.building_number = form.cleaned_data['building_number']
        Cust.phone = form.cleaned_data['phone']
        Cust.nip = form.cleaned_data['nip']
        Cust.headquaters = form.cleaned_data['headquaters']
        Cust.active = True
        Cust.save()
        return redirect("list-customers")
