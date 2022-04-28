from pickle import FALSE
from tabnanny import verbose
from django.db import models
from django.forms import FloatField

# Create your models here.


class Sales(models.Model):
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    commentaries = models.TextField(null=True, blank=True)
    customer = models.ForeignKey('customers.Customers', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    is_credit = models.BooleanField(null=False, blank=False, default=False)
    payment_method = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'sales' # this is the name of the table in the database
        verbose_name = 'Sale' # this is the name of the model in the admin site
        verbose_name_plural = 'Sales' # this is the name of the model in the admin site
        ordering = ['id'] # this is the default ordering of the model
        
    def __str__(self):
        return f'Sale ID: {self.id}'
    
    
class SaleDetails(models.Model):
    sale = models.ForeignKey('sales.Sales', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    amount = models.FloatField()
    total = models.FloatField(null=False, blank=False, default=0)
    price = models.FloatField(null=False, blank=False, default=0)
    discount = models.FloatField(null=False, blank=False, default=0)
    
    class Meta:
        db_table = 'sales_details' # this is the name of the table in the database
        verbose_name = 'Sale Detail' # this is the name of the model in the admin site
        verbose_name_plural = 'Sale Details' # this is the name of the model in the admin site
        ordering = ['id'] # this is the default ordering of the model
        
    def __str__(self):
        return f'Sale: {self.sale.id} - Product: {self.product.name}'

