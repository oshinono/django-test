from django.contrib import admin

from orders.models import Order
from orders.forms import OrderAdminForm
from items.models import Item
from django.contrib.admin.widgets import FilteredSelectMultiple

class Media:
    js = (
        'admin/js/jquery.init.js',
        'js/order_form.js',
    )
    
    css = {
        'all': ('css/order_form.css',)
    }



class CustomFilteredSelectMultiple(FilteredSelectMultiple):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # Добавляем data-currency и кастомное отображение для каждого товара
        context['widget']['attrs']['data-currency'] = {
            str(item.id): item.currency for item in Item.objects.all()
        }
        context['widget']['attrs']['data-display'] = {
            str(item.id): f"{item.name} ({item.currency})" for item in Item.objects.all()
        }
        return context

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_currencies']
    list_filter = ['items__currency']
    search_fields = ['items__name', 'items__description']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = [] 
    ordering = ['created_at']
    date_hierarchy = 'created_at'
    show_facets = True
    show_filters = True
    show_results_per_page = True
    show_pagination = True
    form = OrderAdminForm
    filter_horizontal = ['items', 'taxes', 'discounts']
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'items':
            kwargs['widget'] = CustomFilteredSelectMultiple('Items', False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_currencies(self, obj):
        currencies = {item.currency for item in obj.items.all()}
        return ', '.join(currencies) if currencies else 'Нет товаров' 

    get_currencies.short_description = 'Currency'

