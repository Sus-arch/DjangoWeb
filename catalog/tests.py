from django.test import Client, TestCase


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
