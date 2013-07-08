from django.forms import ModelForm, Textarea
from linde_returns.models import SheetReturn
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class SheetReturnForm(forms.ModelForm):
    class Meta:
        model = SheetReturn
        #fields = ['customer_number' ,'name' ,'address', 'phone', 'headquaters', 'active']


class SearchFrom(forms.Form):
    search_field = forms.CharField(max_length=100)

class SheetReturnsForm(forms.Form):
    sheet_return = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=SheetReturn.objects.all().values_list('id', 'id'))

    sheet_return_archival = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=SheetReturn.objects.all().values_list('id', 'id'))