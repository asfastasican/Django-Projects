from django import forms
from .models import *

class StudentForm(forms.Form):
    name=forms.CharField( max_length=30, required=True)
    marks=forms.IntegerField()
    
    #Explicit validation for name
    def clean(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Len is less than 4") 
        marks=self.cleaned_data['marks']
        if marks>100:
            raise forms.ValidationError("Marks should be between 0-100")
        
class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        

