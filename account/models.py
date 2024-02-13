from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class User(AbstractUser):
    # Дополнительные поля
    date_of_birth = models.DateField(blank=True, null=True)
