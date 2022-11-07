from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/index.html'

    return render(request, template_name)


def item_detail(request, pk: int):
    template_name = 'catalog/item.html'
    context = {'pk': str(pk)}

    return render(request, template_name, context)
