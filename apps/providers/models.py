from django.db import models

# Create your models here.

class Providers (models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    rfc = models.CharField(max_length=13, null= False, blank = False)
    address= models.CharField(max_length=200, null=False, blank=True)
    phone = models.CharField(max_length=18, null=False, blank=True)
    email = models.CharField(max_length=20, null=False, blank=True)

    class Meta:
        db_table= "providers"
        verbose_name= "providers"
        verbose_name_plural="providers"
        ordering=["id"]
    
    def _str_(self):
        return self.name


