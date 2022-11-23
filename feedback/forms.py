from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        exclude = (
            Feedback.id.field.name,
            Feedback.created_on.field.name,
        )
        labels = {
            Feedback.name.field.name: 'Имя',
            Feedback.text.field.name: 'Текст фидбека',
            Feedback.mail.field.name: 'Электронная почта',
        }
        help_texts = {
            Feedback.name.field.name: 'Введите ваше имя',
            Feedback.text.field.name: 'Введите текст фидбека',
            Feedback.mail.field.name: 'Введите ваш адрес электронной почты',
        }
