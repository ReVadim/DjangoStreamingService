from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from src.videos.models import Video
from src.djangoflix.db.models import PublishStateOptions


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_1 = Video.objects.create(title='Test title', description='Test description', video_id='test_1')
        self.obj_2 = Video.objects.create(
            title='Another Test title', video_id='test_2', state=PublishStateOptions.PUBLISH
        )

    def test_valid_title(self):
        title = 'Test title'
        queryset = Video.objects.filter(title=title)
        self.assertTrue(queryset.exists())

    def test_slug_field(self):
        title = self.obj_1.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_1.slug)

    def test_created_count(self):
        queryset = Video.objects.all()
        self.assertEqual(queryset.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(publish_timestamp__lte=now)  # lte '<=' last than equal
        self.assertTrue(published_qs.exists())
        self.assertEqual(qs.count(), 1)

    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        self.assertTrue(published_qs.exists())
