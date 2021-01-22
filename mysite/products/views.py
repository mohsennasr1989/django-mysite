from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets
from .forms import ProductForm
from .models import Products

# def products(request):
#     products_list = Products.objects.all()
#     context = {
#         'products_list': products_list,
#     }
#     return render(request, 'products/index.html', context)
from .serializers import ProductSerializer


def paginated_products_list(request):
    products = Products.objects.all()
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'products/index.html', {'products_list' : products})


class ProductsViewClass(ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products_list'


class ProductsDetailViewClass(DetailView):
    model = Products
    template_name = 'products/detail.html'


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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class PipeFittingsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(category='PIPE_FITTING')
    serializer_class = ProductSerializer


class ValvesViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(category='VALVE')
    serializer_class = ProductSerializer


class ManifoldViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(category='MANIFOLD')
    serializer_class = ProductSerializer


class UFHViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(category='UFH')
    serializer_class = ProductSerializer


class ToolsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter(category='TOOL')
    serializer_class = ProductSerializer
