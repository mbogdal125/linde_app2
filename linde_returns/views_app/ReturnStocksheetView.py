from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import FormView 
from django.contrib.auth.decorators import permission_required
from django.forms.formsets import BaseFormSet
from linde_app2.models import StockSheet, StockItem, Stocktaking, StocktakingStatus, StockSheetStatus
from linde_returns.models import SheetReturn 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.formsets import formset_factory
from datetime import datetime
from linde_returns.forms import SheetReturnForm

class ReturnStocksheetView(FormView):
    model = SheetReturn 
    fields = ['return_type']
    form_class = SheetReturnForm
    template_name = "linde_returns/returnstocksheet.html"
    
    def form_valid(self, form):
        if "stocksheet_number" in self.kwargs:
            ssheet = get_object_or_404(StockSheet, stock_sheet_number=self.kwargs['stocksheet_number'])
            ssheet.status = get_object_or_404(StockSheetStatus, id=100)
            ssheet.save()
            newret = SheetReturn()
            newret.return_type = form.cleaned_data['return_type']
            newret.operator_id = self.request.user.id
            newret.sheet_number = ssheet 
            newret.save()
        return redirect('returns-chose-stocktaking')
