from django.db import models

# Create your models here.
class Product(models.Model):
    official_or_not_description=models.CharField(max_length=37)
    name=models.CharField(max_length=128)
    description=models.CharField(max_length=2048)
    price = models.IntegerField()
    image_url=models.CharField(max_length=256)