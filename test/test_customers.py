#from django.apps import apps
import pytest

#from apps.customers.models import Customers

@pytest.mark.django_db
def test_customers_creation():
    customer = Customers.objects.create(
    name="juanito",
    rfc="VECJ880326RFC",
    address="miguel aleman #233",
    phone="644-16-16-016",
    email="juanito@gmail.com"
    )
    assert customer.name =="juanito"