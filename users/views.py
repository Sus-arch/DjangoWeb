from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import CustomUserCreationForm


def singup(request):
    template = 'users/singup.html'

    form = CustomUserCreationForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(reverse('homepage:home'))

    return render(request, template, context)
