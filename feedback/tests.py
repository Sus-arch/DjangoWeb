from django.test import Client, TestCase
from django.urls import reverse

from feedback.forms import FeedbackForm


class FeedbackFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_feedback_show_correct_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_name_label(self):
        name_label = FeedbackFormTests.form.fields['name'].label
        self.assertEqual(name_label, 'Имя')

    def test_text_label(self):
        text_label = FeedbackFormTests.form.fields['text'].label
        self.assertEqual(text_label, 'Текст фидбека')

    def test_mail_label(self):
        mail_label = FeedbackFormTests.form.fields['mail'].label
        self.assertEqual(mail_label, 'Электронная почта')

    def test_name_help_text(self):
        name_help_text = FeedbackFormTests.form.fields['name'].help_text
        self.assertEqual(name_help_text, 'Введите ваше имя')

    def test_text_help_text(self):
        text_help_text = FeedbackFormTests.form.fields['text'].help_text
        self.assertEqual(text_help_text, 'Введите текст фидбека')

    def test_mail_help_text(self):
        mail_help_text = FeedbackFormTests.form.fields['mail'].help_text
        self.assertEqual(mail_help_text, 'Введите ваш адрес электронной почты')

    def test_create_feedback(self):
        form_data = {
            'name': 'Тест',
            'text': 'Тест',
            'mail': '123@l.com',
        }

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )

        self.assertRedirects(response, reverse('feedback:feedback'))
