from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import (
        Sales,
        SaleDetails,
    )
from ..products.models import (
        Products, 
        Categories
    )


# Form to create sales
class SalesForm(forms.ModelForm):
    
    class Meta:
        model = Sales
        
        fields = [
            'date',
            'commentaries',
            'customer',
            'user',
        ]
        
        labels = {
            'date': 'Fecha',
            'commentaries': 'Comentarios',
            'customer': 'Cliente',
            'user': 'Usuario',
        }
    
        widgets = {
            'user': forms.HiddenInput(),
            'customer': forms.HiddenInput(),
        }


    def __init__(self, *args, **kwargs):
        user = self.user
        customer = kwargs.pop('customer')
        super(SalesForm, self).__init__(*args, **kwargs)
        
        self.fields['user'].required = True
        self.fields['user'].initial = user
        
        self.fields['customer'].required = False
        self.fields['customer'].initial = customer
        
        
# Form set to create sale details
class SaleDetailsForm(forms.ModelForm):
    class Meta:
        model = SaleDetails
        
        fields = [
            'sale',
            'product',
            'amount',
            'total',
            'price',
        ]
        
        labels = {
            'sale': 'Venta',
            'product': 'Producto',
            'amount': 'Cantidad',
            'total': 'Total',
        }
        
        
    def clean_product(self):
        """Valida si hay stock

        Raises:
            ValidationError: Error de validación

        Returns:
            _type_: _description_
        """
        product = self.cleaned_data['product']
        amount = self.cleaned_data['amount']
        if product.stock < amount:
            raise ValidationError('El producto no tiene suficiente stock')
        return product