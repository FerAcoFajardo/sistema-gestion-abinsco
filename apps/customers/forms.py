from django import forms
from django.core.exceptions import ValidationError

from .models import Customers


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        
        labels = {
            'name': 'Nombre',
            'rfc': 'RFC',
            'address': 'Dirección',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
            'max_credit': 'Crédito máximo',
            'actual_deb': 'Deuda actual',
        }
        
        widgets = {
            'max_credit': forms.NumberInput(attrs={'min':'0'}),
            'actual_deb': forms.NumberInput(attrs={'min':'0'}),
        }
        