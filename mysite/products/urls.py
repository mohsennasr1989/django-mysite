from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.products, name='index'),
    path('<int:product_code>/', views.product_detail, name='detail'),
    path('add_product/', views.add_product, name='add'),
    path('edit/<int:product_code>/', views.edit_product, name='edit'),
    path('remove/<int:product_code>/', views.remove_product, name='remove'),
]