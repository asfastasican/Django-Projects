from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    empno=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    address=models.CharField(max_length=50)    
    
    def __str__(self):
        return self.name