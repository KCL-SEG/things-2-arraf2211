"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from .models import *

# Create your forms here.
class Things_Form(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name','description','quantity']
    
