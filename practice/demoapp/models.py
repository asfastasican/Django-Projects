from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Name=models.CharField(max_length=50)
    Roll=models.IntegerField()
    City=models.CharField(max_length=50)
    
