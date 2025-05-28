from django.urls import path
from .views import items_page, item_page

urlpatterns = [
    path('items/', items_page, name='items'),
    path('item/<uuid:id>', item_page, name='item'),
]