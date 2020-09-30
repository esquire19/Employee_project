from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=12)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)


class Admin(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)