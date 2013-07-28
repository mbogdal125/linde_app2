from django.db import models
from linde_app2.models import Customer, StockSheet
from django.contrib.auth.models import User, UserManager
from datetime import datetime
# Create your models here.


class SheetReturn(models.Model):

    RETURN_TYPE = (
        ('NN', 'Nieznany'),
        ('WP', 'Wyprowadzil sie'),
        ('ODM', 'Odmowil przyjecia'),
    )
    sheet_number = models.ForeignKey(StockSheet)
    return_date = models.DateField(default=datetime.now())
    operator = models.ForeignKey(User)
    return_type = models.CharField(max_length=10, choices=RETURN_TYPE)
    archival = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    def __unicode__(self):
        return u"%s" % self.sheet_number
