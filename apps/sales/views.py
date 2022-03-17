from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory

from .models import Sales, SaleDetails
from .forms import SalesForm, SaleDetailsForm
from ..customers.models import Customers

from pprint import pprint

# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'sales/index.html'
    model = Sales
    context_object_name = 'sales'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CreateView(LoginRequiredMixin, View):
    template = 'sales/create.html'
    succes_url = reverse_lazy('sales:index')
    
    
    def get(self,request, pk):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # print(self.get_form_kwargs(pk=pk))
        form_kwargs = self.get_form_kwargs(pk=pk)
        form = SalesForm(initial=form_kwargs)
        customer = form_kwargs.get('customer')
        # form_details = SaleDetailsForm(initial=form_kwargs)
        
        SaleDetailsFormset = formset_factory(SaleDetailsForm, extra=2)
        formset = SaleDetailsFormset(form_kwargs=form_kwargs)
        
        return render(request, self.template, {'form': form, 'customer':customer, 'formset': formset})
    
    
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
        form_kwargs = self.get_form_kwargs(pk=customer_id)
        form = SalesForm(request.POST, initial = form_kwargs)
        # form_details = SaleDetailsForm(request.POST, initial = form_kwargs)
        SaleDetailsFormset = formset_factory(SaleDetailsForm, extra=2)
        formset = SaleDetailsFormset(request.POST,form_kwargs=form_kwargs)
        
        if form.is_valid() :
            # Creación de una venta
            sale = form.save()
            
            total_price = 0
            # print(len(formset))
            for form_details in formset:
                # print(f'{form_details=}')
                print(f'{form_details.is_valid()=}')
                if form_details.is_valid():
                    # Creación de un detalle de venta
                    details = form_details.save(commit=False)
                    total_price += details.price
                    details.sale = sale
                    # details.product
                    details.save()
                    
                    # amount = form_details.cleaned_data['amount']
                    # total = form_details.cleaned_data['total']
                    # price = form_details.cleaned_data['price']
                    # product = form_details.cleaned_data['product']
            
            
                    # sale_detail = SaleDetails(
                    #     sale=sale,
                    #     product=product,
                    #     amount=amount,
                    #     total=total,
                    #     price=price,
                    # )
                    
                    # sale_detail.save()
                        
                
                else:
                    print(f'{form.errors=}')
                    print(f'{form_details.errors=}')
                    self.form_invalid(form, formset)
            else: 
                print(f'{form.errors=}')
                print(f'{formset.errors=}')
                self.form_invalid(form, formset)
            sale.total = total_price
            sale.save()
            return redirect(self.succes_url)
        else:
            print(f'{form.errors=}')
            print(f'{form_details.errors=}')
            return self.form_invalid(form, formset)
        
        
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
    
    
    
    def form_invalid(self, form, formset):
        """_summary_

        Args:
            form (SalesForm): _description_
            form_details (SaleDetailsForm): _description_

        Returns:
            _type_: _description_
        
        """
        return render(self.request, self.template, {'form': form, 'formset': formset})