#-*- coding: utf-8 -*
from django.forms import ModelForm
from django.db import models
from linde_app2.models import Stocktaking
from datetime import datetime

def custom_datefield_for_form(f):
	field = f.formfield()
	if isinstance(f, models.DateField):
		field.widget.format ='%Y-%m-%d'
		field.widget.attrs.update({'class':'datepicker', 'value':datetime.today().strftime('%Y-%m-%d'), 'data-date-format':'yyyy-mm-dd'})
	return field

class GenStocktakingForm(ModelForm):
	formfield_callback = custom_datefield_for_form
	class Meta:
		model = Stocktaking
		fields = ['type', 'date']
    
