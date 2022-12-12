from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description = models.TextField(max_length=200)
    image = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Portfolio(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    tags = models.TextField(max_length=100)
    image = models.TextField(max_length=100)
    urlgithub = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Email(models.Model):
    email = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    sended_at = models.DateTimeField(auto_now_add=True)

class Visiter(models.Model):
    ip_address = models.TextField(max_length=20)
    city = models.TextField(max_length=30)
    country = models.TextField(max_length=30)
    country_code = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)