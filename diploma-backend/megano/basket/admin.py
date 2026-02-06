from django.contrib import admin

from .models import Basket

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = 'pk', 'user',
    list_display_links = 'pk', 'user'
    search_fields = 'user',
    fieldsets = [
        (None, {
            'fields': ('user', 'product')
        }),
    ]
