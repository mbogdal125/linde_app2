from linde_returns.models import SheetReturn
from linde_returns.forms import SheetReturnForm
from linde_app.models import InsertOperation, AgreeOperation, ApproveOperation
from linde_returns import models
from django.views.generic import CreateView, ListView, FormView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormMixin, BaseCreateView
from django.views.generic.list import MultipleObjectMixin
from linde_returns.forms import SearchFrom, SheetReturnsForm
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django import forms
from django.http import HttpResponseRedirect


class SearchReturns(FormMixin, MultipleObjectMixin, TemplateResponseMixin, View):
    form_class = SearchFrom
    template_name = 'linde_returns/search_return.html'
    model = SheetReturn

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))
    def get_success_url(self, **kwargs):
        return reverse('return-preview', kwargs={'customer_number': int(str(self.kwargs['customer_number']))})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        queryset = self.get_queryset()
        num = form.cleaned_data['search_field']
        self.kwargs['customer_number'] = num
        return super(SearchReturns, self).form_valid(form)

    def get_number_sheet_custom(self, client_number):
        queryset_objects = SheetReturn.objects.filter(id_customer__customer_number=int(client_number))
        return queryset_objects
search_returns = SearchReturns.as_view()

class SheetReturnFormView(CreateView):
    model = SheetReturn
    form_class = SheetReturnForm



    def form_valid(self, form):
        sheet_number = form.cleaned_data['sheet_number']
        if not self.check_if_in_stock(sheet_number):
            if self.check_if_in_returns(sheet_number):
                self.save_as_archival(sheet_number)
                print self.save_as_archival(sheet_number)
                #return self.render_to_response(self.get_context_data(form=form))
                messages.error(self.request, "Poprzedni zwrot o tym samym numerze arkusza zostal zarchiwizowany",fail_silently=True)
                self.object = form.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                self.object = form.save()
                return HttpResponseRedirect(self.get_success_url())

        else:
            messages.error(self.request, "Arkusz zostal juz zaksiegowany",fail_silently=True)
            #return HttpResponseRedirect(self.get_success_url())
            return self.render_to_response(self.get_context_data(form=form))
        #return result
    def save_as_archival(self, sheet_number):
        returned = SheetReturn.objects.filter(sheet_number__stock_sheet_number=sheet_number)
        for sheet in returned:
            sheet.archival=True
            sheet.save()


    def check_if_in_returns(self, sheet_number):
        returned = SheetReturn.objects.filter(sheet_number__stock_sheet_number=sheet_number)
        if len(returned)>0:
            return True
        else:
            return False

    def check_if_in_stock(self, sheet_number):
        inserted =InsertOperation.objects.filter(sheet_id__stock_sheet_number=sheet_number)
        agreed = AgreeOperation.objects.filter(sheet_id__stock_sheet_number=sheet_number)
        approved = ApproveOperation.objects.filter(sheet_id__stock_sheet_number=sheet_number)
        if len(inserted)>0:
            return True
        elif len(agreed)>0:
            return True
        elif len(approved)>0:
            return True
        else:
            return False

    def get_success_url(self, **kwargs):
        return reverse('sheet-return-form')


    def form_invalid(self, form):
        result = super(SheetReturnFormView, self).form_invalid(form)
        #messages.error(self.request,"Wypelnij poprawnie pola.",fail_silently=True)
        return result



sheet_return_form = SheetReturnFormView.as_view()

class ReturnPreview(FormView):
    template_name = "linde_returns/sheet_returns_preview.html"
    form_class = SheetReturnsForm


    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        customer_number = self.kwargs['customer_number']
        print customer_number
        form = super(ReturnPreview, self).get_form(form_class)
        #form.fields['sheets'] = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=Privilege.objects.all().values_list('id', 'privilege'))
        form.fields['sheet_return'] = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=SheetReturn.objects.filter(sheet_number__stock_sheet_number=int(customer_number)).filter(archival=False).values_list('sheet_number', 'sheet_number'))
        form.fields['sheet_return_archival'] = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=SheetReturn.objects.filter(sheet_number__stock_sheet_number=int(customer_number)).filter(archival=True).values_list('sheet_number', 'sheet_number'))
        print form.fields['sheet_return']
        return form
return_preview = ReturnPreview.as_view()
