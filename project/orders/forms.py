from django import forms

from orders.models import Order


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_items(self):
        items = self.cleaned_data.get('items')
        if items:
            currencies = {item.currency for item in items}
            if len(currencies) > 1:
                raise forms.ValidationError(
                    "Все товары в заказе должны иметь одинаковую валюту."
                )
        return items