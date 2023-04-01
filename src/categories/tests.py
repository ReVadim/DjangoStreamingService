from django.test import TestCase
from src.categories.models import Category
from src.playlists.models import Playlist


class CategoryTestCase(TestCase):
    def setUp(self):
        category_1 = Category.objects.create(title='Action', slug='action')
        category_2 = Category.objects.create(title='Comedy', slug='comedy', active=False)
        playlist_1 = Playlist.objects.create(title='Test title', category=category_1)
        self.cat_1 = category_1
        self.cat_2 = category_2

    def test_is_active(self):
        self.assertTrue(self.cat_1.active)

    def test_not_active(self):
        self.assertFalse(self.cat_2.active)

    def test_categories_count(self):
        self.assertEqual(Category.objects.all().count(), 2, 'Count Fail')

    def test_categories_slug(self):
        self.assertEqual(self.cat_2.slug, 'comedy')

    def test_related_playlist(self):
        qs = self.cat_1.playlists.all()
        self.assertEqual(qs.count(), 1)
