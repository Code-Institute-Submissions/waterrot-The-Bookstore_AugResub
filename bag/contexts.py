from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            # get the extra price for the diffent format
            extra_price = int(product.format)
            # the price for an item
            item_price = product.price + extra_price
            # get the total price per line
            total += item_data * item_price
            total_price_item = float(item_data * item_price)
            price_per_item = float(item_price)
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total_price_item': total_price_item,
                'price_per_item': price_per_item,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for format, quantity in item_data['items_by_format'].items():
                # get the extra price for the diffent format
                extra_price = int(format)
                # the price for an item
                item_price = product.price + extra_price
                # get the total price per line
                total += quantity * item_price
                total_price_item = float(quantity * item_price)
                price_per_item = float(item_price)
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'format': format,
                    'total_price_item': total_price_item,
                    'price_per_item': price_per_item,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
