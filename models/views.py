from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class ModelListView(ListView):
    model = models.Model
    template_name = 'model_list.html'
    context_object_name = 'models'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ModelCreateView(CreateView):
    model = models.Model
    template_name = 'model_create.html'
    form_class = forms.ModelForm
    success_url = reverse_lazy('model_list')


class ModelDetailView(DetailView):
    model = models.Model
    template_name = 'model_detail.html'


class ModelUpdateView(UpdateView):
    model = models.Model
    template_name = 'model_update.html'
    form_class = forms.ModelForm
    success_url = reverse_lazy('model_list')
    

class ModelDeleteView(DeleteView):
    model = models.Model
    template_name = 'model_delete.html'
    success_url = reverse_lazy('model_list')