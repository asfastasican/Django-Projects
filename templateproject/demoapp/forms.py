from django import forms
from .models import Employee
from django.forms import ModelForm
from django.contrib.auth.models import User


class EmpForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    salary=forms.FloatField()
    address=forms.CharField()

class EmpModelForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
        #fields = ['field 1' , ' field2' ] it will include these fields
        #Exclude = [ ' field1 ',' field2 ']  # it will include these fields

