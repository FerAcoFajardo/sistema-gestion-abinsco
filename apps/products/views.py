from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Products
from .forms import ProductForm

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'products/index.html'
    model = Products
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Products
    success_url = reverse_lazy('products:index')
    

class EditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'products/update.html'
    form_class = ProductForm
    model = Products
    success_url = reverse_lazy('products:index')
    

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'products/delete.html'
    model = Products
    success_url = reverse_lazy('products:index')