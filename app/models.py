from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100, null=False)
    employee_email = models.EmailField(max_length=100, null=False)
    employee_address = models.CharField(max_length=200, null=False)
    employee_phone_no = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.employee_name