from django.shortcuts import render

from catalog.models import Item


def home(request):
    template_name = 'homepage/index.html'
    item = (Item.objects.published()
            .filter(is_on_main=True)
            .order_by('name'))
    context = {
        'items': item
    }

    return render(request, template_name, context)
