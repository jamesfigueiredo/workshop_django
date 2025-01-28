from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')
        serie_number = self.request.GET.get('serie_number')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        if category:
            queryset = queryset.filter(category__id=category)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        return queryset


class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'


class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')