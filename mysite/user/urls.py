from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.users, name='index'),
    path('edit/<int:user_id>/', views.edit_user, name='edit'),
]
