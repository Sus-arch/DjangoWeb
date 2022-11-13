from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    fixtures = ['catalog/fixtures/objeckts.json']

    def test_homepage_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 5)