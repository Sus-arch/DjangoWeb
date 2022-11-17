from django.shortcuts import render

from catalog.items_services import get_item, get_items


def item_list(request):
    template_name = 'catalog/index.html'
    item = get_items()
    context = {
        'items': item
    }

    return render(request, template_name, context)


def item_detail(request, pk: int):
    template_name = 'catalog/item.html'
    item = get_item(pk)
    context = {'item': item}

    return render(request, template_name, context)
