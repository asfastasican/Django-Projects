from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['todo_title','todo_description','is_done']
    
    #For validating the data (any field can be validated)     
    def validate(self,validated_data):   
        title=validated_data.get('todo_title')
        #try:
        #    obj=Todo.objects.get(todo_title=title)
        #   raise serializers.ValidationError("The Title Already Present in Data Base")
        #except:
        #    print("Data is good to go")
        
        if title.isalpha():
            raise serializers.ValidationError("The Title is not Alpha")
        return validated_data
    
    #for validating the specific field
    def validate_todo_title(self,data):
        if len(data)<3:
            raise serializers.ValidationError("The Length of Title is less tha  three")
        return data