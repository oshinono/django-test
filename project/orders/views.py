
import uuid
from django.shortcuts import render, get_object_or_404
from config import settings
from orders.models import Order
def get_order(request, order_id: uuid.UUID):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {
        'order': order,
        'STRIPE_PUBLISHABLE_KEY': settings.stripe_publishable_key
    })

def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {
        'orders': orders
    })