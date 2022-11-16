from django.test import Client, TestCase
from django.urls import reverse

from core.tests import check_content_value


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    fixtures = ['data.json']

    def test_homepage_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 4)

    def test_homepage_show_correct_content(self):
        response = Client().get(reverse('homepage:home'))
        for item in response.context['items']:
            check_content_value(self, item)
