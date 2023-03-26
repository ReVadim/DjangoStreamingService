from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from src.playlists.models import Playlist
from src.videos.models import Video
from src.djangoflix.db.models import PublishStateOptions


class PlaylistModelTestCase(TestCase):
    def create_videos(self):
        video_1 = Video.objects.create(title='Video_title', video_id='123abc')
        video_2 = Video.objects.create(title='Second_title', video_id='456def')
        video_3 = Video.objects.create(title='Third_title', video_id='789ghj')
        self.video = video_1
        self.video_2 = video_2
        self.video_3 = video_3

    def setUp(self):
        self.create_videos()
        self.obj_1 = Playlist.objects.create(
            title='Test title', description='Test description', video=self.video
        )
        obj_2 = Playlist.objects.create(
            title='Another Test title', state=PublishStateOptions.PUBLISH, video=self.video
        )
        # obj_2.videos.set([self.video, self.video_2, self.video_3])
        video_queryset = Video.objects.all()
        obj_2.videos.set(video_queryset)
        obj_2.save()
        self.obj_2 = obj_2

    def test_playlist_video(self):
        self.assertEqual(self.obj_1.video, self.video)

    def test_playlist_video_items(self):
        count = self.obj_2.videos.all().count()
        self.assertEqual(count, 3)

    def test_video_playlist_ids_property(self):
        ids = self.obj_1.video.get_playlist_ids()
        actual_ids = list(Playlist.objects.filter(video=self.video).values_list('id', flat=True))
        self.assertEqual(ids, actual_ids)

    def test_video_playlist(self):
        qs = self.video.playlist_featured.all()
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
