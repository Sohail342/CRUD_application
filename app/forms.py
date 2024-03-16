from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:  
        model = Employee  
        fields = ['employee_name', 'employee_email', 'employee_address', 'employee_phone_no']
