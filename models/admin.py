from django.contrib import admin
from . import models


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(models.Model, ModelAdmin)