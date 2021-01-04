from django import forms
from django.db import models
from .models import Employee



class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'