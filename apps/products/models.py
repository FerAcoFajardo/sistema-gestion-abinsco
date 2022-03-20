from django.db import models
from random import randrange

# Create your models here.

def random_image_chooser():
    """This defines the default image for the user"""
    images = [
        'products/generic/131-1312918_png-file-svg-product-icon-transparent-png.png',
        'products/generic/img_566093.png'
    ]
    i = randrange(2)
    return images[i]

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
    image = models.ImageField(upload_to='profiles/', max_length=255, null=True, blank=True, default=random_image_chooser())

    def validate_in_storage(self, value):
        if self.in_storage >= value:
            return "Estas vendiendo mas de la existencia en inventario"

    class Meta:
        db_table = "products"
        verbose_name = "products"
        verbose_name_plural ="products"
        ordering = ["id"]

    def __str__(self):
        return self.name


  