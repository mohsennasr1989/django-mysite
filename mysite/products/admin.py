from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'specification', 'size')
    search_fields = ('id', 'code', 'name', 'specification', 'size')
    list_filter = ('id', 'code', 'name', 'specification', 'size')
