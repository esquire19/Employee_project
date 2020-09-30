from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
   
    path('employeereg', views.employee_form,name='form'),
    
    path('list', views.employee_list,name='list'),

    path('<int:id>', views.employee_form,name='update'),

    path('delete/<int:id>', views.employee_delete,name='delete'),

    path('adminlogin',views.admin_login,name="admin_login"),

    path('adminRegister',views.admin_register,name="admin_register")
    
]