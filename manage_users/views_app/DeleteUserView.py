from django.views.generic import CreateView, TemplateView, DeleteView
from linde_app2.models import Customer, GasCylinderGroup, GasCylinderType, StockSheet, StockItem, InsertOperation, Stocktaking, StockSheetStatus
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.views.generic import edit
from django.views.generic import base
from django.views.generic.list import BaseListView
from linde_app2 import models
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
