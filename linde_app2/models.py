from django.db import models
from django.contrib.auth.models import User, UserManager
from datetime import datetime
from django import forms



def insert_role(self):
    if User.objects.filter(username=self.username).filter(usergroup__id_group__groupprivilege__privilege__privilege__exact="insert_data"):
        return True


def data_manager(self):
    if User.objects.filter(username=self.username).filter(usergroup__id_group__groupprivilege__privilege__privilege__exact='data_manager'):
        return True
    User.add_to_class("insert_role", insert_role)
    User.add_to_class("data_manager", data_manager)



class Customer(models.Model):
    customer_number = models.CharField(max_length = 100, unique=True)
    name = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    postalcode = models.IntegerField(max_length = 6)
    flat_number = models.IntegerField()
    building_number = models.IntegerField()
    phone = models.CharField(max_length = 100)
    nip = models.CharField(max_length = 100)
    headquaters = models.BooleanField()
    active = models.BooleanField()
    def __unicode__(self):
        return u"%s" % self.customer_number

class StockSheet(models.Model):
    stock_sheet_number = models.CharField(max_length = 20, unique=True)
    id_customer = models.ForeignKey('Customer')
    id_stocktaking = models.ForeignKey('Stocktaking')
    notes = models.TextField()
    status = models.ForeignKey('StockSheetStatus')
    stockTakingDate = models.DateField()
    archival = models.BooleanField(default=False)

    def get_absolute_url(self):
        return u''

    def __unicode__(self):
        return u"%s" % self.stock_sheet_number

class GenerateStockTaking(models.Model):
    stock_taking = models.ForeignKey('Stocktaking')
    operator = models.ForeignKey(User)
    date = models.DateField(default=datetime.now())

class InsertOperation(models.Model):
    sheet_id = models.ForeignKey('StockSheet')
    operator = models.ForeignKey(User)
    date = models.DateField(default=datetime.now())


class AgreeOperation(models.Model):
    sheet_id = models.ForeignKey('StockSheet')
    operator = models.ForeignKey(User)
    date = models.DateField(default=datetime.now())

class ApproveOperation(models.Model):
    sheet_id = models.ForeignKey('StockSheet')
    approve_operator = models.ForeignKey(User)
    approve_date = models.DateField(default=datetime.now())

class StockSheetStatus(models.Model):
    description = models.TextField()
    class Meta:
        verbose_name_plural = "StockSheetStatus"
    def __unicode__(self):
        return u"%s" % self.description


class StockItem(models.Model):
    id_stock_sheet = models.ForeignKey('StockSheet')
    id_gas_cylinder_type = models.ForeignKey('GasCylinderType')
    amount_real = models.IntegerField()
    amount_real_agreed = models.IntegerField(default=0)
    amount_sap = models.IntegerField(default=0)
    amount_sap_agreed = models.IntegerField(default=0)
    def __unicode__(self):
        return u"%s" % self.id_gas_cylinder_type

class GasCylinderType(models.Model):
    description = models.TextField()
    id_gas_cylinder_group = models.ForeignKey('GasCylinderGroup')
    gas_cylinder_typecol = models.CharField(max_length = 45)
    def __unicode__(self):
        return self.description

class GasCylinderGroup(models.Model):
    description = models.TextField()
    active = models.BooleanField()
    def __unicode__(self):
        return u"%s" % self.description



class UserGroup(models.Model):
    id_user = models.ForeignKey(User)
    id_group = models.ForeignKey('Group')
    def __unicode__(self):
        return u"%s" % self.id_user

class Group(models.Model):
    group_name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.group_name
class GroupPrivilege(models.Model):
    group = models.ForeignKey("Group");
    privilege = models.ForeignKey("Privilege");
    def __unicode__(self):
        return u"%s %s" % (self.group, self.privilege)

class Privilege(models.Model):

    privilege = models.CharField(max_length = 45)
    def __unicode__(self):
        return u"%s" % self.privilege


class Stocktaking(models.Model):
    stocktaking_number = models.IntegerField()
    type = models.ForeignKey('StocktakingType')
    date = models.DateField()
    status = models.ForeignKey('StocktakingStatus')
    active = models.BooleanField()
    def __unicode__(self):
        return u"%s" % self.stocktaking_number

class StocktakingType(models.Model):
    description = models.TextField()
    def __unicode__(self):
        return u"%s" % self.description


class StocktakingStatus(models.Model):
    description = models.TextField()

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = "StocktakingStatus"


