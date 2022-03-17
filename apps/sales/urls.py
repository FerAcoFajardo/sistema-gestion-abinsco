from django.urls import path
from . import views

app_name = 'sales'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    
    path('create/<int:pk>/', views.CreateView.as_view(), name='create'),    
    # User and Registration urls
]