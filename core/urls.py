from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('authentication.urls')),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', views.home, name='home'),
    
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('models.urls')),
    path('', include('products.urls')),
    path('', include('sales.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)