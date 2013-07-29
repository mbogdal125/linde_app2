#-*- coding: utf-8 -*
from django.views.generic import ListView
from django.views.generic.edit import FormView
from linde_app2.models import GasCylinderGroup
from manage_data.forms import AddGasGroupForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

class GasGroups(ListView):
    template_name = "manage_data/gascylindergroups.html"
    model = GasCylinderGroup

class AddGasGroup(FormView):
    form_class = AddGasGroupForm
    template_name = "manage_data/add_gascylindergroup.html"

    def form_valid(self, form):
        GasGroup = GasCylinderGroup()
        GasGroup.description = form.cleaned_data['description']
        GasGroup.active = form.cleaned_data['active']
        GasGroup.save()
        return redirect("list-gasgroups")
