from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    start_date = models.DateField()
    position = models.CharField()
    salary = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10)
