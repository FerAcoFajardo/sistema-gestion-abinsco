from djanjo.apps import apps
import pytest
from apps.products.models import Products

@pytest.mark.django_db

def tast_product_creation():
    product = Products.objects.create(
        name = "Soldadura"
        description = "Soldadura tradicional con plomo y sin plomo en una variedad de longitudes y diámetros"
        current_price = 25.00
        in_storage =  15
        code = 'ABC1

        category = "Tools"
        unity = ''
    )
    assert.product.name == "Soldadura"


    )ngdef teang