from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from brands.views import *
from categories.views import *
from products.views import *
from sales.views import *
from models.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('models/list/', ModelListView.as_view(), name='model_list'),
    path('models/create/', ModelCreateView.as_view(), name='model_create'),
    path('models/<int:pk>/detail/', ModelDetailView.as_view(), name='model_detail'),
    path('models/<int:pk>/update/', ModelUpdateView.as_view(), name='model_update'),
    path('models/<int:pk>/delete/', ModelDeleteView.as_view(), name='model_delete'),

    path('categories/list/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('sales/list/', SaleListView.as_view(), name='sale_list'),
    path('sales/create/', SaleCreateView.as_view(), name='sale_create'),
    path('sales/<int:product_id>/create/', SaleProductCreateView.as_view(), name='sale_product'),
    path('sales/<int:pk>/detail/', SaleDetailView.as_view(), name='sale_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)