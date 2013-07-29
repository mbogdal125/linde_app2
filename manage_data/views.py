#-*- coding: utf-8 -*
from manage_data.views_app.Customers import Customers, AddCustomer
from manage_data.views_app.GasCylinderTypes import GasTypes, AddGasType
from manage_data.views_app.GasCylinderGroups import GasGroups, AddGasGroup

customers = Customers.as_view()
add_customer = AddCustomer.as_view()
gas_types = GasTypes.as_view()
add_gas_type = AddGasType.as_view()
gas_groups = GasGroups.as_view()
add_gas_group = AddGasGroup.as_view()
