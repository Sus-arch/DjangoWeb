from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


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


def user_list(request):
    template = 'users/user_list.html'
    users = (
        User.objects.all()
        .filter(is_active=True)
        .values('username',
                'email',
                'first_name',
                'last_name',
                'birthday')
    )

    context = {
        'users': users
    }

    return render(request, template, context)


def user_detail(request, pk: int):
    template = 'users/user_detail.html'
    search_user = get_object_or_404(
        User.objects.values('username',
                            'email',
                            'first_name',
                            'last_name',
                            'birthday'),
        pk=pk,
    )

    context = {
        'user': search_user
    }

    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'

    form = CustomUserChangeForm(request.POST or None, instance=request.user)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Изменения сохранены')
        return redirect(reverse('users:profile'))

    return render(request, template, context)
