from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from feedback.forms import FeedbackForm
from feedback.models import Feedback


def feedback(request):
    template = 'feedback/index.html'

    form = FeedbackForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        send_mail(
            f'Привет {form.cleaned_data["name"]}',
            f'{form.cleaned_data["text"]}',
            'from@example.com',
            [form.cleaned_data['mail']],
            fail_silently=True,
        )
        item = Feedback.objects.create(
            **form.cleaned_data
        )
        item.save()
        messages.success(request, 'Фидбек оправлен. Спасибо!')
        return redirect(reverse('feedback:feedback'))

    return render(request, template, context)
