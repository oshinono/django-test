from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'currency', 'created_at', 'updated_at']
    list_filter = ['currency', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'currency']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = []
    ordering = ['created_at']
    date_hierarchy = 'created_at'
    show_facets = True
    show_filters = True
    show_results_per_page = True
    show_pagination = True