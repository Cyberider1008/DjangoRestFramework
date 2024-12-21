from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    name = models.CharField(max_length =100)
    age = models.IntegerField(default=10)
    email = models.EmailField()

    def __str__(self):
     return self.name
    