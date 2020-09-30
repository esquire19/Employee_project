from django.shortcuts import render, redirect
from .form import EmployeeForm, AdminForm
from django.contrib import messages 
from .models import Employee, Admin
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
   

# Create your views here.
def employee_list(request):
     if request.user.is_anonymous:
        return redirect('/login')
     else:
        context = {'employee_list':Employee.objects.all()}
        return render(request,'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:  
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save() 
        return redirect('/list')
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')

def admin_login(request):

        if request.method == 'POST':
            email = adminform.cleaned_data.get('email')
            password = adminform.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                adminform = login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
       
        adminform = AuthenticationForm()
        return render(request,'admin/admin_login.html',{'adminform':adminform})


def admin_register(request):
    if request.method == 'POST':
        adminform = AdminForm(request.POST)
        if adminform.is_valid(): 
            adminform.save() 
            username = adminform.cleaned_data.get('firstname') 
            email = adminform.cleaned_data.get('email') 
            ######################### mail system ####################################  
            mail_subject = 'Registration successfully.'
            message = 'Thank You !! U have successfully registered.'
            email = EmailMessage(mail_subject, message, to=[email]) 
            email.send() 
            return redirect('/adminlogin') 
    else: 
        adminform = AdminForm()
        return render(request,'admin/admin_register.html',{'adminform':adminform})  


def index(request):
    return render(request,'index.html')