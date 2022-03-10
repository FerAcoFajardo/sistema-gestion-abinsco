from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False)
    rfc = models.CharField(max_length=13, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=True)
    phone = models.CharField(max_length=10, null=False, blank=True)
    email = models.EmailField(null=False, blank=True)
    # credit = models.ForeignKey('credit.Credit', on_delete=models.CASCADE)
    sale = models.ForeignKey('sales.Sales', on_delete=models.CASCADE)

    class Meta:
        db_table = "customers"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ['id']
        
    def __str__(self):
        return self.name