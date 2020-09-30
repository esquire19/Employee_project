
from django import forms
from employee_register.models import Employee,Admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name','mobile','emp_code','position')
        labels = {
            'name': 'Full Name',
            'emp_code': 'Emp. Code'
            
        }
    
    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required = False

class AdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = ('firstname','lastname','email','mobile','password')
        