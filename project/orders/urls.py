from django.urls import path
from .views import get_order, get_orders

urlpatterns = [
    path('order/<uuid:order_id>', get_order, name='order'),
    path('orders', get_orders, name='orders')
]