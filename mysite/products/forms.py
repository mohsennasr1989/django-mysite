from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['code', 'name', 'specification', 'size', 'singular_unit', 'plural_unit', 'package_quantity', 'image']
