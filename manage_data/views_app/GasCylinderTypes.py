#-*- coding: utf-8 -*
from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import GasCylinderType 
from manage_data.forms import AddGasTypeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

class GasTypes(ListView):
    template_name = "manage_data/gascylindertypes.html"
    model = GasCylinderType 

class AddGasType(FormView):
    form_class = AddGasTypeForm
    template_name = "manage_data/add_gascylindertype.html"

    def form_valid(self, form):
        GasType = GasCylinderType()
        GasType.description = form.cleaned_data['description']
        GasType.id_gas_cylinder_group = form.cleaned_data['id_gas_cylinder_group']
        GasType.gas_cylinder_typecol = form.cleaned_data['gas_cylinder_typecol']
        GasType.save()
        return redirect("list-gastypes")
