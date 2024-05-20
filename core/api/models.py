from django.db import models

# Create your models here.
class Car_info(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    