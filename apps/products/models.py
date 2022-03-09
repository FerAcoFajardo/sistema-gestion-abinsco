from django.db import models

# Create your models here.


UNITY_CHOICES = [
    ('pz', 'PZ'),
    ('kg', 'KG'),
]

class Categories (models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    current_price = models.FloatField(null=False, blank=False)
    in_storage = models.IntegerField(null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    unity = models.CharField(max_length=20,choices=UNITY_CHOICES, default='pz' ,null=False, blank=False) # Enum

    class Meta:
        db_table = "products"
        verbose_name = "products"
        verbose_name_plural ="products"
        ordering = ["id"]

    def __str__(self):
        return self.name


  