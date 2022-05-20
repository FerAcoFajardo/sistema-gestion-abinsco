from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _("%(value)s is not positive."),
            params={"value": value}
        )


class PositiveDecimalField(models.DecimalField):
    description = _("Número decimal positivo")

    @cached_property
    def validators(self):
        return super().validators + [validate_positive]


class Customers(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False)
    rfc = models.CharField(max_length=13, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=False, blank=True)
    phone = models.CharField(max_length=18, null=False, blank=True, validators=[RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')])
    email = models.EmailField(null=False, blank=True)
    max_credit = models.FloatField(null=True, blank=True, default=0)
    actual_deb = models.FloatField(null=True, blank=True, default=0)
    # credit = models.ForeignKey('credit.Credit', on_delete=models.CASCADE)
    # sale = models.ForeignKey('sales.Sales', on_delete=models.CASCADE)

    class Meta:
        db_table = "customers"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ['id']
        
    def __str__(self):
        return self.name