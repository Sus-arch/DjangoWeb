from django.shortcuts import get_object_or_404

from catalog.models import Item


def get_item(pk):
    item = get_object_or_404(Item.objects.published(),
                             pk=pk)

    return item


def get_items():
    item = (Item.objects.published()
            .order_by('category__name'))

    return item
