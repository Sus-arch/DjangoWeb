from catalog.models import Item


def get_items():
    item = (Item.objects.published()
            .filter(is_on_main=True)
            .order_by('name'))

    return item
