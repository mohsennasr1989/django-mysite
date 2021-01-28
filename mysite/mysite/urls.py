"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_view

router = routers.SimpleRouter()
router.register('products', product_view.ProductViewSet)
router.register('pipe-fittings', product_view.PipeFittingsViewSet)
router.register('valve', product_view.ValvesViewSet)
router.register('manifold', product_view.ManifoldViewSet)
router.register('ufh', product_view.UFHViewSet)
router.register('tools', product_view.ToolsViewSet)

app_name = 'my_site'
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls, name='admin'),
    path('user/', include('user.urls', namespace='user')),
    path('product/', include('products.urls', namespace='product')),
    path('signup/', user_view.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='products/index.html'), name='logout'),
    path('profile/', user_view.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
