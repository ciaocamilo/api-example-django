from itertools import product
from django.db import models

# Create your models here.
# Comentario casual dos

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_picture = models.CharField(max_length=200)
    product_description = models.CharField(max_length=300)