from django.shortcuts import render

from homepage.items_services import get_items


def home(request):
    template_name = 'homepage/index.html'
    item = get_items()
    context = {
        'items': item
    }

    return render(request, template_name, context)
