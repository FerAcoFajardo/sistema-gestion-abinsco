from django.db.models.signals import pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db import transaction

from ..sales.models import Sales, SaleDetails


# Signals pare quitar el stock de los productos
@receiver(post_save, sender=SaleDetails)
def update_stock(sender, instance, **kwargs):
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_

    Returns:
        _type_: _description_
    """
    with transaction.atomic():
        instance.product.in_storage -= instance.amount
        instance.product.save()