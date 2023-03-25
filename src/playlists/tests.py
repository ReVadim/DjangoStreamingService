from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Playlist
from src.videos.models import Video
from src.djangoflix.db.models import PublishStateOptions


class PlaylistModelTestCase(TestCase):
    def setUp(self):
        video_1 = Video.objects.create(title='Video_title', video_id='123abc')
        self.video = video_1
        self.obj_1 = Playlist.objects.create(
            title='Test title', description='Test description', video=self.video
        )
        self.obj_2 = Playlist.objects.create(
            title='Another Test title', state=PublishStateOptions.PUBLISH, video=self.video
        )

    def test_playlist_video(self):
        self.assertEqual(self.obj_1.video, self.video)

    def test_video_playlist(self):
        qs = self.video.playlist_set.all()
        self.assertTrue(qs.count(), 2)

    def test_valid_title(self):
        title = 'Test title'
        queryset = Playlist.objects.filter(title=title)
        self.assertTrue(queryset.exists())

    def test_slug_field(self):
        title = self.obj_1.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_1.slug)

    def test_created_count(self):
        queryset = Playlist.objects.all()
        self.assertEqual(queryset.count(), 2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Playlist.objects.filter(publish_timestamp__lte=now)  # lte '<=' last than equal
        self.assertTrue(published_qs.exists())
        self.assertEqual(qs.count(), 1)

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        self.assertTrue(published_qs.exists())
