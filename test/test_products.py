
import pytest

from django.apps import apps
from apps.products.models import Products,Categories


@pytest.mark.django_db
def test_product_creation():

    category = Categories.objects.create(
        name = "Tools"
    )

    product = Products.objects.create(
        name = "Soldadura",
        description = "Soldadura tradicional con plomo y sin plomo en una variedad de longitudes y diámetros",
        current_price = 25.00,
        in_storage =  15,
        code = 'ABC1',
        category = Categories.objects.get(id=1),
        unity = 'Kg'
    )
    assert product.name == "Soldadura"


    