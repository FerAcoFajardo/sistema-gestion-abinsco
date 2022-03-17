from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sales, SaleDetails
from .forms import SalesForm, SaleDetailsForm
from ..customers.models import Customers

# Create your views here.

class CreateView(LoginRequiredMixin, View):
    template = 'sales/create.html'
    succes_url = reverse_lazy('sales:list')
    
    
    def get(self,request, pk):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(self.get_form_kwargs(pk=pk))
        form = SalesForm(form_kwargs=self.get_form_kwargs(pk=pk))
        form_details = SaleDetailsForm(form_kwargs=self.get_form_kwargs(pk=pk))
        return render(request, self.template, {'form': form, 'form_details': form_details})
    
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Obtener el id del cliente desde el url
        customer_id = kwargs.get('pk')
        customer = Customers.objects.get(id=customer_id)
        form = SalesForm(request.POST)
        form_details = SaleDetailsForm(request.POST)
        
        if form.is_valid() and form_details.is_valid():
            # Creación de una venta
            sale = form.save()
            total_price = 0
            for detail in form_details.cleaned_data['product']:
                total_price += form_details.cleaned_data['price'][detail]
                sale_detail = SaleDetails(
                    sale=sale,
                    product=detail,
                    amount=form_details.cleaned_data['amount'][detail],
                    total=form_details.cleaned_data['total'][detail],
                    price=form_details.cleaned_data['price'][detail],
                )
                
                sale_detail.save()
                
            sale.total = total_price
            
            return self.succes_url
        else:
            return self.form_invalid(form, form_details)
        
        
    def get_form_kwargs(self, pk, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        # form_kwargs = super(CreateView, self).get_form_kwargs(**kwargs)
        # form_kwargs = {}
        # print(customer_id)
        # print(pk)
        # form_kwargs['customer'] = customer
        # print(f'{user=}')
        # form_kwargs['user'] = user
        
        
        customer_id = pk
        customer = Customers.objects.get(id=customer_id)
        user = self.request.user
        return {'user': user, 'customer': customer}
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = kwargs.pop('pk')
        return context
    
    
    
    def form_invalid(self, form, form_details):
        """_summary_

        Args:
            form (SalesForm): _description_
            form_details (SaleDetailsForm): _description_

        Returns:
            _type_: _description_
        
        """
        return render(self.request, self.template, {'form': form, 'form_details': form_details})