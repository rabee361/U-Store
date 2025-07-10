# from django.db import models
# from django.contrib.auth.models import AbstractUser 
# from utils.types import UserType


# # class CustomUser(AbstractUser):
# #     image = models.ImageField(upload_to='users/images' , null=True, blank=True)
# #     user_type = models.CharField(max_length=10, choices=UserType, default='customer')

# #     USERNAME_FIELD = 'email'

# # class Merchant(models.Model):
# #     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

# # class Customer(models.Model):
# #     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    

# # class Plan(models.Model):
# #     name = 
# #     price = 
# #     feature1 =
# #     feature2 =
# #     feature3 =
# #     type = annual/month

# class Unit(models.Model):
#     name = models.CharField(max_length=50)

# class UnitConversion():
#     pass

# class ProductCategory(models.Model):
#     name = models.CharField(max_length=100)
#     english_name = models.CharField(max_length=100)
#     arabic_name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='products/categories' , null=True, blank=True)

# class Product(models.Model):
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     code = models.CharField(max_length=100, null=True, blank=True)
#     en_name = models.CharField(max_length=100)
#     ar_name = models.CharField(max_length=100, null=True, blank=True)
#     barcode = models.CharField(max_length=300, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     short_description = models.CharField(max_length=200, null=True, blank=True)
#     shipped = models.BooleanField(default=False)
#     tax = models.BooleanField(default=False)
#     # weight = 
#     weight_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     # cost = 
#     max_order_quantity = models.IntegerField(null=True, blank=True)
#     min_order_quantity = models.IntegerField(null=True, blank=True)
#     displayed = models.BooleanField(default=False)
#     price = models.FloatField(null=True, blank=True)
#     color = models.CharField(max_length=100, null=True, blank=True)
#     size = models.CharField(max_length=100, null=True, blank=True)
#     current_quantity = models.IntegerField()

# # class Store(models.Model):
# #     merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
# #     link = models.CharField(max_length=100)
# #     name = models.CharField(max_length=100)

# #     logo = models.ImageField(upload_to='stores/logos' , null=True, blank=True)
# #     banner = models.ImageField(upload_to='stores/banners' , null=True, blank=True)

# # class theme(models.Model):
# #     primary = models.CharField(max_length=10)
# #     secondary = models.CharField(max_length=10)
# #     tertiary = models.CharField(max_length=10)
# #     free = models.BooleanField(default=False)
# #     image = models.ImageField(upload_to='theme/images')
# #     description = models.TextField()
# #     designer = models.CharField(max_length=100)
# #     createdAt = models.DateTimeField(auto_now_add=True)
# #     price = models.FloatField(null=True, blank=True)
# #     # rating = models.IntegerField(validators=[maxValidator(5), minValidator(1)])


# # class Warehouse(models.Model):
# #     merchant
# #     name 
# #     country
# #     city
# #     neighborhood
# #     street
# #     selling_point
# #     long
# #     lat
