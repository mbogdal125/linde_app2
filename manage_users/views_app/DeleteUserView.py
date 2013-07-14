from django.views.generic import CreateView, TemplateView, DeleteView
from linde_app.models import Customer, GasCylinderGroup, GasCylinderType, StockSheet, StockItem, InsertOperation, Stocktaking, StockSheetStatus
from linde_app.forms import CustomerForm, GasCylinderGroupForm, GasCylinderTypeForm,StockSheetForm, StockItemFormSet, SearchFrom, InsertOperationFormSet
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.forms import ModelForm, Textarea
from django.views.generic import ListView, FormView
from django.views.generic import edit
from django.views.generic import base
from django.views.generic.list import BaseListView
from linde_app import models
from django.db.models import Q
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormMixin, BaseCreateView
from django.views.generic.list import MultipleObjectMixin
from django.db import connection
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User


class DeleteUserView(DeleteView):
    model = User


    def get_success_url(self, **kwargs):
        return reverse('home')