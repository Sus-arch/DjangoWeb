from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    template_name = 'catalog/index.html'
    item = (Item.objects.published()
            .order_by('category__name'))
    context = {
        'items': item
    }

    return render(request, template_name, context)


def item_detail(request, pk: int):
    template_name = 'catalog/item.html'
    item = get_object_or_404(Item.objects.published(),
                             pk=pk)
    context = {'item': item}

    return render(request, template_name, context)
