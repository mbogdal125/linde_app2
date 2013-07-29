#-*- coding: utf-8 -*
from django.forms import ModelForm
from linde_app2.models import Customer, GasCylinderType, GasCylinderGroup

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = ['name', 'name2', 'street', 'city', 'postalcode', 'flat_number', 'building_number', 'phone', 'nip', 'headquaters', 'sin_num']
    def __init__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)
        self.fields['flat_number'].required = False
        self.fields['building_number'].required = False
        self.fields['name2'].required = False
    
class AddGasTypeForm(ModelForm):
    class Meta:
        model = GasCylinderType
        fields = ['id_gas_cylinder_group', 'gas_cylinder_typecol', 'description']

class AddGasGroupForm(ModelForm):
    class Meta:
        model = GasCylinderGroup
        fields = ['active', 'description']
