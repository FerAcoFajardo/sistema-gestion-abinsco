from email.policy import default
from django.db import models

class Purchases(models.Model):
    order_number = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    provider = models.ForeignKey('providers.Providers', on_delete=models.CASCADE)

    class Meta:
        db_table = "purchases"
        verbose_name = "purchase"
        verbose_name_plural ="purchases"
        ordering = ["id"]

    def __str__(self):
        return self.order_number










class PurchaseDetails(models.Model):
    purchase = models.ForeignKey('purchases.Purchases', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False)
    total =  models.FloatField(null=False, blank=False, default=0)
    price = models.FloatField(null=False, blank=False, default=0)
    discount = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        db_table = "purchase_details"
        verbose_name = 'purchase detail'
        verbose_name_plural = 'purchase details'
        ordering = ["id"]
        
    
    def __str__(self):
        return f'{self.purchase} - {self.product}'