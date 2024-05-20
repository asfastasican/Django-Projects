from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    city=models.CharField(max_length=100,default="BMT")
    
class FeedBackForm(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.AutoField(primary_key=True)
    email=models.EmailField()
    feedback=models.CharField(max_length=1000,null=True)
    
class Studentinfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
        
    
    
    
