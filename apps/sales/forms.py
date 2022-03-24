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

from ..customers.models import (
    Customers,
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
            'total',
        ]
        
        labels = {
            # 'date': 'Fecha',
            'commentaries': 'Comentarios',
            'customer': 'Cliente',
        }
    
        widgets = {
            'user': forms.HiddenInput(), 
            # 'customer': forms.HiddenInput(),
            'commentaries': forms.Textarea(attrs={'class': ''}),
            'total': forms.NumberInput(attrs={'class': 'form-control cart-total-price', 'readonly': 'readonly', 'value':0, 'style':'margin:0 0 0 0;border:0 0 0 0;'}),
        }


    def __init__(self, *args, **kwargs):
        
        
        super(SalesForm, self).__init__(*args, **kwargs)
        
        
        
        self.fields['customer'].required = False

        # self.fields['customer'].queryset = Customers.objects.filter(id=1)
        
        self.fields['customer'].initial = Customers.objects.get(id=1)          
        
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
            'discount'
        ]
        
        labels = {
            # 'sale': 'Venta',
            'product': 'Producto',
            'amount': 'Cantidad',
            'total': 'Total',
            'price': 'Precio',
        }
        
        widgets = {
            'sale': forms.HiddenInput(),
            # Inmutable input            
            'price': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'cart-price cart-column'}),
            'product': forms.HiddenInput(attrs={'class': 'cart-item-title', 'type': 'hidden'}),
            'amount': forms.NumberInput(attrs={'class': 'cart-quantity-input', 'min': '1', 'value': '1'}),
        }
        
        
    
    
    def __init__(self, *args, **kwargs):
        # form_kwargs = kwargs.pop('form_kwargs')
        # customer = form_kwargs.pop('customer')
        # user = form_kwargs.pop('user')
        form_kwargs = kwargs.pop('form_kwargs', None)
        if form_kwargs is not None:
            customer = form_kwargs.pop('customer', None)
            user = form_kwargs.pop('user', None)

        else:
            customer = kwargs.pop('customer', None)
            user = kwargs.pop('user', None)

        super(SaleDetailsForm, self).__init__(*args, **kwargs)
        
        self.fields['sale'].required = False
        self.fields['total'].widget.attrs['readonly'] = True     
        self.fields['price'].widget.attrs['readonly'] = True      