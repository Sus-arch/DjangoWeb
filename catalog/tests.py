from django.test import Client, TestCase
from django.core.exceptions import ValidationError

from .models import Item, Category, Tag


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


class ItemModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Test category',
            slug='test-category-slug',
            weight=300
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='Test tag',
            slug='test-tag-slug'
        )

    def tearDown(self) -> None:
        Item.objects.all().delete()
        super().tearDown()

    def test_unable_create_item(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(
                is_published=True,
                name='Test item',
                category=self.category,
                text='no amazing'
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_item(self):
        item_count = Item.objects.count()

        self.item = Item(
            is_published=True,
            name='Test item',
            category=self.category,
            text='превосходно'
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_able_create_item_with_punctuation_mark(self):
        item_count = Item.objects.count()

        self.item = Item(
            is_published=True,
            name='Test item',
            category=self.category,
            text='превосходно!'
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_able_create_item_with_forgot_space(self):
        item_count = Item.objects.count()

        self.item = Item(
            is_published=True,
            name='Test item',
            category=self.category,
            text='Это очень превосходно!Просто потрясающе'
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)


class CategoryModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Книга',
            slug='test-category-slug',
            weight=300
        )
        cls.category.full_clean()
        cls.category.save()

    def tearDown(self) -> None:
        Category.objects.all().delete()
        super().tearDown()

    def test_unable_create_category_already_exists(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='КНиГа!!',
                slug='another-test-category-slug',
                weight=300
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_unable_create_category_weight_negative_number(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='Test category',
                slug='test-category-slug',
                weight=-1
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_unable_create_category_weight_to_big_number(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='Test category',
                slug='category-slug',
                weight=400000
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_unable_create_category_weight_not_number(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='Test category',
                slug='test-category-slug',
                weight='ten'
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_able_create_category(self):
        category_count = Category.objects.count()

        self.category = Category(
            is_published=True,
            name='Test category',
            slug='category-slug-test',
            weight=200
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(Category.objects.count(), category_count + 1)


class TagModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tag = Tag(
            is_published=True,
            name='Акция',
            slug='tag-slug'
        )
        cls.tag.full_clean()
        cls.tag.save()

    def tearDown(self) -> None:
        Tag.objects.all().delete()
        super().tearDown()

    def test_unable_create_tag_already_exists(self):
        tag_count = Tag.objects.count()

        with self.assertRaises(ValidationError):
            self.tag = Tag(
                is_published=True,
                name='АКЦИЯ!!!!!!!!!!!!!',
                slug='test-slug'
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count)

    def test_able_create_tag(self):
        tag_count = Tag.objects.count()

        self.tag = Tag(
            is_published=True,
            name='Test tag',
            slug='test-tag-slug'
        )
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count + 1)
