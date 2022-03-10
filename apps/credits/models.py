from django.db import models

# Create your models here.

class Credit(models.Model):
    credit_limit = models.FloatField(null=False, blank=False)
    customers = models.ForeignKey('customers.Customers', on_delete=models.CASCADE)