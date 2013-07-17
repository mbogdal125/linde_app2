from django.forms import ModelForm
from linde_app2.models import Stocktaking

class GenStocktakingForm(ModelForm):
    class Meta:
        model = Stocktaking
        fields = ['type', 'date']
    
