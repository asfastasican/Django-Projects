from django import forms
from django.forms import ModelForm
from .models import FeedBackForm

class StudentForm(forms.Form):
    name=forms.CharField(max_length=50, required=False)
    marks=forms.IntegerField(required=False)
    password=forms.CharField(widget=forms.PasswordInput)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FeedBackForm
        fields="__all__"
