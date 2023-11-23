from django.db import models

# Create your models here.
# Category table
class Category(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name_category=models.CharField('קטגוריה',max_length=255)

#Product table
class Product(models.Model):
    id_product = models.IntegerField(primary_key=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='קטגוריה')
    name_product = models.CharField('שם מוצר',max_length=255)
    description_product = models.TextField('תאור')
    price_product = models.DecimalField('מחיר',max_digits=10, decimal_places=2)
    stock_product = models.PositiveIntegerField('מלאי')
    
#Supplier table
class Supplier(models.Model):
    id_supplier = models.IntegerField(primary_key=True)
    name_supplier = models.CharField('שם ספק',max_length=255)
    address_supplier = models.CharField('כתובת',max_length=255)
    phone_number_supplier = models.CharField('מספר טלפון',max_length=255)
#Order table
class Order(models.Model):
    id_order = models.IntegerField(primary_key=True)
    id_product=models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='מוצר')
    id_supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='ספק')
    quantity_order = models.IntegerField('כמות')
    date_order = models.DateTimeField('תאריך')
