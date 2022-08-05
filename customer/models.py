from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from accounts.models import User, CustomerUser, ShopUser
from accounts.permissons import IsCustomer
# Create your models here.


class CustomerQna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)


class CustomerQuestion(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)