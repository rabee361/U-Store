from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.TextChoices):
    CUSTOMER = 'customer'
    MERCHANT = 'merchant'
    ADMIN = 'admin'

class CodeTypes(models.TextChoices):
    SIGNUP = 'SIGNUP'
    RESET_PASSWORD = 'RESET_PASSWORD'
    FORGET_PASSWORD = 'FORGET_PASSWORD'

class BusinessTypes(models.TextChoices):
    FASHION = 'fashion'
    ELECTRONICS = 'electronics'
    FOOD = 'food'
    BOOKS = 'books'
    HOME = 'home'
    BEAUTY = 'beauty'
    SPORTS = 'sports'
    TOYS = 'toys'

class StoreTypes(models.TextChoices): 
    RETAIL = 'retail'
    WHOLESALE = 'wholesale'
    MANUFACTURING = 'manufacturing'
    SERVICES = 'services'
    DIGITAL = 'digital'