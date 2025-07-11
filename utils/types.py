from django.db import models


class UserType(models.TextChoices):
    CUSTOMER = 'customer'
    MERCHANT = 'merchant'
    ADMIN = 'admin'