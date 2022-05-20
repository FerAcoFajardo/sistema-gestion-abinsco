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
        
        def clean_phone(self):
            phone = self.cleaned_data.get('phone')
            print('miau')
            # Regex to validate phone number
            phone_regex = r'(\\+?52[\\s\\-]?)'
            if phone and not phone.matches(phone_regex):
                raise forms.ValidationError('El número de teléfono debe de comenzar con +')
            return phone
        