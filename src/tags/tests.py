from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from src.tags.models import TaggedItem
from django.db.utils import IntegrityError
from src.playlists.models import Playlist


class TaggedItemTestCase(TestCase):
    def setUp(self):
        playlist_title = "new-title"
        self.playlist_title = playlist_title
        self.playlist_obj = Playlist.objects.create(title=playlist_title)
        self.playlist_obj.tags.add(TaggedItem(tag='test-new-tag'), bulk=False)

    def test_content_type_is_not_null(self):
        with self.assertRaises(IntegrityError):
            TaggedItem.objects.create(tag='new_test_tag')

    def test_create_via_content_type(self):
        c_type = ContentType.objects.get(app_label='playlists', model='playlist')
        tag_1 = TaggedItem.objects.create(content_type=c_type, object_id=1, tag='new-tag')
        self.assertIsNotNone(tag_1.pk)

    def test_create_via_model_content_type(self):
        type_1 = ContentType.objects.get_for_model(Playlist)
        tag = TaggedItem.objects.create(content_type=type_1, object_id=1, tag='test-tag')
        self.assertIsNotNone(tag.pk)

    def test_related_field(self):
        self.assertEqual(self.playlist_obj.tags.count(), 1)

    def test_related_field_create(self):
        self.playlist_obj.tags.create(tag='another-test-tag')
        self.assertEqual(self.playlist_obj.tags.count(), 2)

    def test_related_field_query_name(self):
        qs = TaggedItem.objects.filter(playlist__title__iexact=self.playlist_title)
        self.assertEqual(qs.count(), 1)

    def test_direct_object_creation(self):
        obj = self.playlist_obj
        tag = TaggedItem.objects.create(content_object=obj, tag='another-tag')
        self.assertIsNotNone(tag.pk)
