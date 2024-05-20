from rest_framework import serializers

class Car_infoSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    country=serializers.CharField(max_length=100)
    