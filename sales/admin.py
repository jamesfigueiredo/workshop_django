from django.contrib import admin
from . import models


class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity',)
    search_fields = ('product',)

admin.site.register(models.Sale, SaleAdmin)