from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers


from .models import Sales, SaleDetails
from .forms import SalesForm, SaleDetailsForm
from ..customers.models import Customers
from ..products.models import Products

from pprint import pprint
import json

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
    message = 'La venta se ha registrado correctamente'
    
    
    def get(self,request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # print(self.get_form_kwargs(pk=pk))
        
        form_kwargs = self.get_form_kwargs()
        form = SalesForm(initial={'user': self.request.user})
        # customer = form_kwargs.get('customer')
        
        #form_details = SaleDetailsForm(initial=form_kwargs)
        
        SaleDetailsFormset = formset_factory(SaleDetailsForm, extra=0)
        formset = SaleDetailsFormset(form_kwargs=form_kwargs)
        
        # context = self.get_context_data()
        context = {}
        
        context['form'] = form
        context['formset'] = formset
        
        return render(request, self.template, context)

    def get_context_data(self, **kwargs):
        context = {}
        context["customer"] = Customers.objects.get(id=1) 
        context["user"] = self.request.user 
        return context
    
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        # context = self.get_context_data(self,**kwargs)
        # Obtener el id del cliente desde el url
        # customer_id = request.POST.get('customer')
        # print(f'{customer_id=}')
        form_kwargs = self.get_form_kwargs()
        form = SalesForm(request.POST)
        SaleDetailsFormset = formset_factory(SaleDetailsForm, extra=0)
        formset = SaleDetailsFormset(request.POST)
        
        
        if form.is_valid() and formset.is_valid():
            # Creación de una venta
            sale = Sales.objects.create(
                commentaries = form.cleaned_data['commentaries'],
                user = self.request.user,
                customer = form.cleaned_data['customer'] if form.cleaned_data['customer'] else Customers.objects.get(id=1),
            )
            total_price = 0
            print(formset)
            for form_details in formset:
                if form_details.is_valid():
                    details = form_details.save(commit=False)
                    total_price += details.total
                    details.sale = sale
                    details.save()
                    
                        
                
                else:
                    self.form_invalid(form, formset)
            else: 
                self.form_invalid(form, formset)
            sale.total = total_price
            sale.save()
            
            messages.success(request,self.message)
            return redirect(self.succes_url)
        else:
            return self.form_invalid(form, formset)
        
        
    def get_form_kwargs(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        # customer_id = pk
        # customer = Customers.objects.get(id=customer_id)
        user = self.request.user
        return {'user': user}
    
    
    
    def form_invalid(self, form, formset):
        """_summary_

        Args:
            form (SalesForm): _description_
            form_details (SaleDetailsForm): _description_

        Returns:
            _type_: _description_
        
        """
        # context = self.get_context_data(self)
        context = {}
        context['form'] = form
        context['formset'] = formset
        print(f'{form.errors=}')
        print(f'{formset.errors=}')
        return render(self.request, self.template, context)
    
    
# View to get a product from id and return a json
def get_product_by_id(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'GET':
        
        product = Products.objects.get(id=pk)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.current_price,
            'stock': product.in_storage,
            'image': product.image.url,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET method is allowed', 'status':418})



def get_products_by_name(request):
    if request.method == 'GET':
        try:
            name = request.GET['term']
        except Exception as err:
            return JsonResponse(json.dumps(''), safe= False)

        products = Products.objects.filter(name__icontains=name).values()
        # Cast queryset to list
        products_list = list(products)
        data = []
        for product in products_list:
            format = {
                'id': product['id'],
                'text': product['name']
            }
            data.append(format)
        # Cast list to json
        products_json = json.dumps(data)
        #Queryset
        return JsonResponse(products_json, safe = False )
    else:
        return JsonResponse({'error': 'Only GET method is allowed', 'status':418})    

# View to get a customer from id and return a json
def get_customer_by_id(request, pk):
    if request.method == 'GET':
        customer = Customers.objects.get(id=pk)
        
        data = {
            'name': customer.name,
            'rfc': customer.rfc,
            'address': customer.address,
            'phone': customer.phone,
            'email': customer.email,
        }
        
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET method is allowed', 'status':418})

# View to get a customer list from name and return a json
def get_customers_by_name(request):
    if request.method == 'GET':
        try:
            name = request.GET['term']
        except Exception as err:
            #return JsonResponse(json.dumps(''), safe= False)
            name = ""
        

        customers = Customers.objects.filter(name__icontains=name).values()
        # Parece que en lugar de only, se puede usar values_list, el pedo es que regresa una tupla
        customers = list(customers)
        
        customersFormat = []
        for customer in customers:
            formato = {
                'id': customer['id'],
                'text': customer['name']
            }
            
            customersFormat.append(formato)

               
        #data = serializers.serialize("json", customers)
        data = json.dumps(customersFormat)
        # Cast queryset to list
        # customers_list = list(customers)
        # Cast list to json
        # customers_json = json.dumps(customers_list)
        #Queryset
        return JsonResponse(data, safe = False )
    else: 
        return JsonResponse({'error': 'Only GET method is allowed', 'status':418})

def get_customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all().values()
        customers_list = list(customers)
        # Cast list to json
        customers_json = json.dumps(customers_list)
        #Queryset
        return JsonResponse(customers_json, safe = False )
    else:
        return JsonResponse({'error': 'Only GET method is allowed', 'status':418})