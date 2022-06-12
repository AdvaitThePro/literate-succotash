from django.db import models

class Product(models.Model):
    title: str
    description: str
    
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class User(models.Model):
    user: str
    items_bought: str

    user = models.CharField(max_length=435)
    items_bought = models.CharField(max_length=10000)
