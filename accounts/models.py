from django.db import models
from django.contrib.auth.models import AbstractUser 
from utils.types import UserType
from dashboard.models import *


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
    
