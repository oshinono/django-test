
import uuid
from django.shortcuts import render, get_object_or_404
from config import settings
from collections import Counter
from orders.models import Order
def get_order(request, order_id: uuid.UUID):
    order = get_object_or_404(Order, id=order_id)

    order_currency = order.items.first().currency
    if order_currency == 'USD':
        publishable_key = settings.stripe_usd_publishable_key
    elif order_currency == 'RUB':
        publishable_key = settings.stripe_rub_publishable_key
    else:
        raise ValueError(f'{order_currency} не поддерживается')

    return render(request, 'orders/order.html', {
        'order': order,
        'currency': order_currency,
        'STRIPE_PUBLISHABLE_KEY': publishable_key
    })

def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {
        'orders': orders
    })