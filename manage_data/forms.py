from django.forms import ModelForm
from linde_app2.models import Customer, GasCylinderType, GasCylinderGroup

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer 
        fields = ['name', 'street', 'city', 'postalcode', 'flat_number', 'building_number', 'phone', 'nip', 'headquaters']
    
class AddGasTypeForm(ModelForm):
    class Meta:
        model = GasCylinderType
        fields = ['id_gas_cylinder_group', 'gas_cylinder_typecol', 'description']

class AddGasGroupForm(ModelForm):
    class Meta:
        model = GasCylinderGroup
        fields = ['active', 'description']
