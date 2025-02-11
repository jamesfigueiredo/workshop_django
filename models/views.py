from rest_framework import generics
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class ModelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Model
    template_name = 'model_list.html'
    context_object_name = 'models'
    permission_required = 'models.view_model'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ModelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Model
    template_name = 'model_create.html'
    form_class = forms.ModelForm
    success_url = reverse_lazy('model_list')
    permission_required = 'models.add_model'


class ModelDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Model
    template_name = 'model_detail.html'
    permission_required = 'models.view_model'


class ModelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Model
    template_name = 'model_update.html'
    form_class = forms.ModelForm
    success_url = reverse_lazy('model_list')
    permission_required = 'models.change_model'
    

class ModelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView,):
    model = models.Model
    template_name = 'model_delete.html'
    success_url = reverse_lazy('model_list')
    permission_required = 'models.delete_model'
    
    
class ModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer
    
    
class ModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer