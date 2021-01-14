from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.users, name='index'),
    path('<int:user_id>/', views.user_detail, name='detail'),
    path('add_user/', views.add_user, name='add'),
    path('edit/<int:user_id>/', views.edit_user, name='edit'),
    path('remove/<int:user_id>/', views.remove_user, name='remove'),
]
