from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    salary=models.FloatField()
    address=models.CharField(max_length=100)

class Demo(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    

