from django.test import TestCase
from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='Test title', description='Test description')

    def test_valid_title(self):
        title = 'Test title'
        queryset = Video.objects.filter(title=title)
        self.assertTrue(queryset.exists())
