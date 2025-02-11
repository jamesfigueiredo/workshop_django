from rest_framework import generics
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        Product = self.request.GET.get('Product')
        category = self.request.GET.get('category')
        serie_number = self.request.GET.get('serie_number')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if Product:
            queryset = queryset.filter(Product__id=Product)

        if category:
            queryset = queryset.filter(category__id=category)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        return queryset


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'
    

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
    
    
class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer