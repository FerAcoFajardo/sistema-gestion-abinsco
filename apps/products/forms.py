from django import forms

from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
        exclude = ('image',)
        
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'current_price': 'Precio actual',
            'in_storage': 'En existencia',
            'code': 'Código',
            'category': 'Categoría',
            'unit': 'Unidad',
            'image': 'Imagen',
        }
        
        widgets = {
            'current_price': forms.NumberInput(attrs={'min':'0'}),
        }