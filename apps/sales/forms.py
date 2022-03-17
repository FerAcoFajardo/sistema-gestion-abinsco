from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models as mod

from .models import (
        Sales,
        SaleDetails,
    )

from ..products.models import (
        Products, 
        Categories
    )


from pprint import pprint

# Form to create sales
class SalesForm(forms.ModelForm):
    
    class Meta:
        model = Sales
        
        fields = [
            #'date',
            'customer',
            'user',
            'commentaries',
        ]
        
        labels = {
            # 'date': 'Fecha',
            'commentaries': 'Comentarios',
            'customer': 'Cliente',
            'user': 'Usuario',
        }
    
        widgets = {
            'user': forms.HiddenInput(),
            'customer': forms.HiddenInput(),
        }


    def __init__(self, *args, **kwargs):
        # form_kwargs = kwargs.pop('form_kwargs')
        customer = kwargs.pop('customer', None)
        user = kwargs.pop('user', None)
        super(SalesForm, self).__init__(*args, **kwargs)
        
        self.fields['user'].required = True
        if user is not None:
            self.fields['user'].initial = user
        
        self.fields['customer'].required = False
        if customer is not None:
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
        
        widgets = {
            'sale': forms.HiddenInput(),
        }
        
        
    def clean_product(self):
        """Valida si hay stock

        Raises:
            ValidationError: Error de validación

        Returns:
            _type_: _description_
        """
        product = self.cleaned_data['product']
        # pprint(self.cleaned_data)
        amount = self.data['amount']
        amount = int(amount)
        if product.in_storage < amount:
            raise ValidationError('El producto no tiene suficiente stock')
        return product
    
    
    def __init__(self, *args, **kwargs):
        # form_kwargs = kwargs.pop('form_kwargs')
        # customer = form_kwargs.pop('customer')
        # user = form_kwargs.pop('user')
        super(SaleDetailsForm, self).__init__(*args, **kwargs)
        
        self.fields['sale'].required = False
        