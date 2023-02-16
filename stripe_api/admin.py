from django.contrib import admin
from stripe_api.models import Item


@admin.register(Item)
class ModelAdmin(admin.ModelAdmin):
    pass
