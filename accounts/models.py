from django.db import models
from django.contrib.auth.models import AbstractUser 
from utils.types import UserType


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users/images' , null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=UserType, default=UserType.CUSTOMER)
    email = models.EmailField(max_length=255, unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

class Merchant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    rate = models.FloatField()

# class CurrencyConversion(models.Model):
#     first_currency = 
#     second_currency = 
#     value = 

class Plan(models.Model):
    pass
    # name = 
    # price = 
    # feature1 =
    # feature2 =
    # feature3 =
    # type = annual/month

class Unit(models.Model):
    name = models.CharField(max_length=50)

class UnitConversion():
    pass

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    ar_name = models.CharField(max_length=100)
    en_description = models.TextField(null=True, blank=True)
    ar_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/categories' , null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)

class Product(models.Model):
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
    cost_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    max_order_quantity = models.IntegerField(null=True, blank=True)
    min_order_quantity = models.IntegerField(null=True, blank=True)
    displayed = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    current_quantity = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)


class StoreCurrnecy(models.Model):
    pass

class Store(models.Model):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    logo = models.ImageField(upload_to='stores/logos' , null=True, blank=True)
    banner = models.ImageField(upload_to='stores/banners' , null=True, blank=True)

class StoreDomain(models.Model):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

class theme(models.Model):
    primary = models.CharField(max_length=10)
    secondary = models.CharField(max_length=10)
    tertiary = models.CharField(max_length=10)
    free = models.BooleanField(default=False)
    image = models.ImageField(upload_to='theme/images')
    description = models.TextField()
    designer = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True, blank=True)
    # rating = models.IntegerField(validators=[maxValidator(5), minValidator(1)])


class Social(models.Model):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)


# class Warehouse(models.Model):
#     merchant
#     name 
#     country
#     city
#     neighborhood
#     street
#     selling_point
#     long
#     lat
