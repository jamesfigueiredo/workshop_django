from django.urls import path
from . import views

urlpatterns = [
    path('models/list/', views.ModelListView.as_view(), name='model_list'),
    path('models/create/', views.ModelCreateView.as_view(), name='model_create'),
    path('models/<int:pk>/detail/', views.ModelDetailView.as_view(), name='model_detail'),
    path('models/<int:pk>/update/', views.ModelUpdateView.as_view(), name='model_update'),
    path('models/<int:pk>/delete/', views.ModelDeleteView.as_view(), name='model_delete'),
    
    path('api/v1/models/', views.ModelListCreateAPIView.as_view(), name='category-list-create-api-view'),
    path('api/v1/models/<int:pk>/', views.ModelRetrieveUpdateDestroyAPIView.as_view(), name='category-update-delete-api-view'),
]