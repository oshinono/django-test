import uuid
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Item

def items_page(request):
    items = Item.objects.all()
    return render(request, 'items/items.html', {
        'items': items
    })

def item_page(request, id: uuid.UUID):
    item = get_object_or_404(Item, id=id)
    return render(request, 'items/item.html', {
        'item': item,
    })