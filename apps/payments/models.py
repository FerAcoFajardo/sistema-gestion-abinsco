from pickle import FALSE
from tabnanny import verbose
from django.db import models
from django.forms import FloatField

# Create your models here.

class Payments(models.Model):
    date = models.DateField(auto_now=True, auto_now_add=False)
    total = models.FloatField(null=True, blank=True)
    customers = models.ForeignKey('customers.Customers', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'payments' # this is the name of the table in the database
        verbose_name = 'Payment' # this is the name of the model in the admin site
        verbose_name_plural = 'Payments' # this is the name of the model in the admin site
        ordering = ['id'] # this is the default ordering of the model
        
    def __str__(self):
        return f'Payment ID: {self.id}'

class PaymentsDetails(models.Model):
    payment = models.ForeignKey('payments.Payments', on_delete=models.CASCADE)
    sale = models.ForeignKey('sales.Sales', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'payments_details' # this is the name of the table in the database
        verbose_name = 'Payment Detail' # this is the name of the model in the admin site
        verbose_name_plural = 'Payments Details' # this is the name of the model in the admin site
        ordering = ['id'] # this is the default ordering of the model
        
    def __str__(self):
        return f'Payment: {self.payment.id} - Sale: {self.sale.id}'