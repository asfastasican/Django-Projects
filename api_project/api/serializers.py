from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validate_date):
        instance.name=validate_date.get('name',instance.name)
        instance.roll=validate_date.get('roll',instance.roll)
        instance.city=validate_date.get('city',instance.city)
        instance.save()
        return instance
    
class MStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=['id','name','roll','city']
        
        
class EmpSerializer(serializers.Serializer):
    emp_id=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    department=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=30)
    company=serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validate_date):
        instance.name=validate_date.get('name',instance.name)
        instance.department=validate_date.get('department',instance.department)
        instance.city=validate_date.get('city',instance.city)
        instance.company=validate_date.get('company',instance.company)
        instance.save()
        return instance
