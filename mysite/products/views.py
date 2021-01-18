from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import ProductForm
from .models import Products


# def products(request):
#     products_list = Products.objects.all()
#     context = {
#         'products_list': products_list,
#     }
#     return render(request, 'products/index.html', context)


class ProductsViewClass(ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products_list'


class ProductsDetailViewClass(DetailView):
    model = Products
    template_name = 'products/detail.html'


# def product_detail(request, product_code):
#     details = Products.objects.get(code=product_code)
#     context = {
#         'product': details,
#     }
#     return render(request, 'products/detail.html', context)


# def add_product(request):
#     form = ProductForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('product:index')
#
#     return render(request, 'products/form.html', {'form': form})


class AddProductViewClass(CreateView):
    model = Products
    fields = ['code', 'name', 'specification', 'size', 'singular_unit', 'plural_unit', 'package_quantity', 'image']
    template_name = 'products/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def edit_product(request, product_code):
    product = Products.objects.get(pk=product_code)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product:index')

    return render(request, 'products/form.html', {'form': form, 'product': product})


def remove_product(request, product_code):
    product = Products.objects.get(pk=product_code)

    if request.method == 'POST':
        product.delete()
        return redirect('product:index')

    return render(request, 'products/remove_confirm.html', {'product': product})
