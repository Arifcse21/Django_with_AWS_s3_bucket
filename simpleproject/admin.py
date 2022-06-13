from django.contrib import admin
from .models import SimpleFormModel
# Register your models here.

@admin.register(SimpleFormModel)
class SimpleFormAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]