from django.db import models
from dashboard.models import *
from accounts.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

class MerchantCurrency(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    parts = models.FloatField()
    parts_name = models.CharField(max_length=10)


# class Plan(models.Model):
#     pass
#     # name = 
#     # price = 
#     # feature1 =
#     # feature2 =
#     # feature3 =
#     # type = annual/month

class ProductCategory(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    en_name = models.CharField(max_length=100)
    ar_name = models.CharField(max_length=100)
    en_description = models.TextField(null=True, blank=True)
    ar_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/categories' , null=True, blank=True)
    slug = models.CharField(max_length=50, null=True, blank=True)

class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True, blank=True)
    en_name = models.CharField(max_length=100)
    ar_name = models.CharField(max_length=100, null=True, blank=True)
    barcode = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    shipped = models.BooleanField(default=False)
    tax = models.BooleanField(default=False)
    weight = models.IntegerField(null=True, blank=True)
    weight_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    cost = models.FloatField(null=True, blank=True)
    cost_currency = models.ForeignKey(MerchantCurrency, on_delete=models.CASCADE)
    max_order_quantity = models.IntegerField(null=True, blank=True)
    min_order_quantity = models.IntegerField(null=True, blank=True)
    displayed = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    current_quantity = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

class Store(models.Model):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='stores/logos' , null=True, blank=True)
    banner = models.ImageField(upload_to='stores/banners' , null=True, blank=True)

# class StoreDomain(models.Model):
#     merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
#     domain = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)

# class Theme(models.Model):
#     primary = models.CharField(max_length=10)
#     secondary = models.CharField(max_length=10)
#     tertiary = models.CharField(max_length=10)
#     image = models.ImageField(upload_to='theme/images')
#     description = models.TextField()
#     designer = models.CharField(max_length=100)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     price = models.FloatField(null=True, blank=True)
#     rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

# class MerchantTheme(models.Model):
#     pass

class MerchantSocial(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

class Warehouse(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    selling_point = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)


class WarehouseMove(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='from_warehouse')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='to_warehouse')
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)