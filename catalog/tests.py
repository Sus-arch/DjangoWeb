from django.test import Client, TestCase
from django.core.exceptions import ValidationError
from .models import Category, Item


class StaticURLTests(TestCase):
    def test_catalog_page_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_number(self):
        response = Client().get('/catalog/2')
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_negative_number(self):
        response = Client().get('/catalog/-3')
        self.assertEqual(response.status_code, 404)

    def test_catalog_page_float_number(self):
        response = Client().get('/catalog/1.3')
        self.assertEqual(response.status_code, 404)

    def test_catalog_page_not_number(self):
        response = Client().get('/catalog/ema')
        self.assertEqual(response.status_code, 404)

    def test_catalog_page_zero(self):
        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)


# class ModelsTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.category = Category.objects.create(name="Тест",
#                                                slug="test-category-slug")
#
#     def test_unable_create_one_letter(self):
#         item_count = Item.objects.count()
#         with self.assertRaises(ValidationError):
#             self.item = Item(name="Тестовый айтем", category=self.category, text="Тествое описание")
#         self.item.full_clean()
#         self.item.save()
#         self.item.tags.add(self.tag)
