from django.contrib import admin
from django.urls import path
from brands import views

urlpatterns = [
    path('admin/', admin.site.urls),
]