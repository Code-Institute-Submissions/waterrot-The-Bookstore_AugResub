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
            # change the price change of the format back to the format name
            if format == '-2':
                item_format = 'ebook'
            elif format == '-1':
                item_format = 'audiobook'
            elif format == '0':
                item_format = 'softcover'
            elif format == '4':
                item_format = 'hardcover'

            # get the extra price for the diffent formats
            extra_price = int(product.format)
            # the price for one item
            item_price = product.price + extra_price
            price_per_item = float(item_price)
            # get the total price per line
            total_price_item = float(item_data * item_price)

            total += item_data * item_price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total_price_item': total_price_item,
                'price_per_item': price_per_item,
                'item_format': item_format,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for format, quantity in item_data['items_by_format'].items():
                # change the price change of the format back to the format name
                if format == '-2':
                    item_format = 'ebook'
                elif format == '-1':
                    item_format = 'audiobook'
                elif format == '0':
                    item_format = 'softcover'
                elif format == '4':
                    item_format = 'hardcover'

                # get the extra price for the diffent formats
                extra_price = int(format)
                # the price for one item
                item_price = product.price + extra_price
                price_per_item = float(item_price)
                # get the total price per line
                total_price_item = float(quantity * item_price)
               
                total += quantity * item_price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'item_format': item_format,
                    'total_price_item': total_price_item,
                    'price_per_item': price_per_item,
                    'format': format,
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
