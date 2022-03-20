from django.urls import path
from . import views

app_name = 'sales'


# the first argument is the url pattern
# the second argument is the view function
# the third argument is the name of the url

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    
    path('create/<int:pk>/', views.CreateView.as_view(), name='create'),    
    # url to get a product
    # path('get_product/<int:pk>/', views.get_product_price_by_id, name='get_product'),
    # url to get products by name
    path('get_product/<int:pk>/', views.get_product_price_by_id, name='get_product'),
    # User and Registration urls
    #url to get product by name
    path('get_product_by_name/<str:name>/',views.get_product_by_name, name = 'get_product_by_name'),

    path('get_customer_by_id/<int:pk>/',views.get_customer_by_id, name = 'get_customer_by_id'),
    path('get_customers_by_name',views.get_customers_by_name, name = 'get_customers_by_name'),
    path('get_customers/',views.get_customers, name = 'get_customers'),
]