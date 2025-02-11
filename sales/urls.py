from django.urls import path
from . import views

urlpatterns = [
    path('sales/list/', views.SaleListView.as_view(), name='sale_list'),
    path('sales/create/', views.SaleCreateView.as_view(), name='sale_create'),
    path('sales/<int:product_id>/create/', views.SaleProductCreateView.as_view(), name='sale_product'),
    path('sales/<int:pk>/detail/', views.SaleDetailView.as_view(), name='sale_detail'),
    
    path('api/v1/sales/', views.SaleCreateListAPIView.as_view(), name='sale-create-list-api-view'),
    path('api/v1/sales/<int:pk>/', views.SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-update-delete-api-view'),
]