import django
django.setup()
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'