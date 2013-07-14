from manage_data.views_app.Customers import Customers, AddCustomer

customers = Customers.as_view()
add_customer = AddCustomer.as_view()
