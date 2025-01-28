from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class SaleListView(ListView):
    model = models.Sale
    template_name = 'sale_list.html'
    context_object_name = 'sales'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('name')

        if product:
            queryset = queryset.filter(product__name__icontains=product)

        return queryset


class SaleCreateView(CreateView):
    model = models.Sale
    template_name = 'sale_create.html'
    form_class = forms.SaleForm
    success_url = reverse_lazy('sale_list')


class SaleDetailView(DetailView):
    model = models.Sale
    template_name = 'sale_detail.html'


class SaleProductCreateView(CreateView):
    model = models.Sale
    template_name = 'sale_product.html'
    form_class = forms.SaleForm
    success_url = reverse_lazy('sale_list')

    def get_context_data(self, **kwargs):
        # Captura o product_id da URL
        product_id = self.kwargs.get('product_id')
        if not product_id:
            raise Http404("Produto não encontrado")
        
        product = get_object_or_404(models.Product, id=product_id)

        # Passa o produto para o contexto
        context = super().get_context_data(**kwargs)
        context['product'] = product
        return context

    def get_initial(self):
        # Captura o product_id da URL
        product_id = self.kwargs.get('product_id')
        if not product_id:
            raise Http404("Produto não encontrado")
        
        product = get_object_or_404(models.Product, id=product_id)

        # Preenche o formulário com o produto e a quantidade 1
        initial_data = {
            'product': product,
            'quantity': 1,  # Definindo a quantidade inicial como 1
        }
        return initial_data

