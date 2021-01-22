from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'firstname', 'lastname', 'cellphone')
    list_filter = ('id', 'user', 'firstname', 'lastname', 'cellphone')
    search_fields = ('id', 'user', 'firstname', 'lastname', 'cellphone')
