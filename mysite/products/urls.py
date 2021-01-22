from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductsViewClass.as_view(), name='index'),
    path('list/', views.paginated_products_list, name='paginated'),
    path('<int:pk>/', views.ProductsDetailViewClass.as_view(), name='detail'),
    path('add_product/', views.AddProductViewClass.as_view(), name='add'),
    path('edit/<int:product_code>/', views.edit_product, name='edit'),
    path('remove/<int:product_code>/', views.remove_product, name='remove'),
]