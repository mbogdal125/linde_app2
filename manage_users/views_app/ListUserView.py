from django.views.generic.list import ListView

from linde_app2.models import User

class ListUserView(ListView):
    template_name = 'manage_users/listuser.html'
    model = User
