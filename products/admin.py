from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'description', 
    'serie_number', 'cost_price', 'selling_price', 'quantity',)
    search_fields = ('name', 'brand', 'category',)

admin.site.register(models.Product, ProductAdmin)