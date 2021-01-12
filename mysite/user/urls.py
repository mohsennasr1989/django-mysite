from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.users, name='users'),
    path('<int:user_id>/', views.user_detail, name='detail'),
    path('add_user/', views.add_user, name='add'),
]
