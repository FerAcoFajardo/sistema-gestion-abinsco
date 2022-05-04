from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Customers
from .forms import CustomersForm

class IndexView(generic.ListView):
    template_name = 'customers/index.html'
    model = Customers
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CreateView(generic.CreateView):
    template_name = 'customers/create.html'
    form_class = CustomersForm
    model = Customers
    success_url = reverse_lazy('customers:index')
    

class EditView(generic.UpdateView):
    template_name = 'customers/update.html'
    form_class = CustomersForm
    model = Customers
    success_url = reverse_lazy('customers:index')