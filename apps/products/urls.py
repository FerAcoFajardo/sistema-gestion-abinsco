from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    
    path('create/', views.CreateView.as_view(), name='create'),    
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete')    
]