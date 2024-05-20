from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    marks=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
class StudentinfoSerizalizer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)
    