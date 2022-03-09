from django.db import models

# Create your models here.


class products (models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    current_price = models.FloatField(null=False, blank=False)
    in_storage = models.IntegerField(null=False, blank=False)
    code = models.CharField(max_lenght=)
