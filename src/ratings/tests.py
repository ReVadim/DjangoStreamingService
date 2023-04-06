from django.test import TestCase
import random
from django.contrib.auth import get_user_model
from src.playlists.models import Playlist
from src.ratings.models import Rating, RatingChoices
from django.db.models import Avg


User = get_user_model()  # User.objects.all()


class RatingTestCase(TestCase):

    def create_playlists(self):
        items = []
        self.playlist_count = random.randint(10, 200)
        for _ in range(0, self.playlist_count):
            items.append(Playlist(title=f'TV_show_{_}'))
        Playlist.objects.bulk_create(items)
        self.playlists = Playlist.objects.all()

    def create_users(self):
        user_list = []
        self.user_count = random.randint(10, 700)
        for i in range(0, self.user_count):
            user_list.append(User(username=f'user_{i}'))
        User.objects.bulk_create(user_list)
        self.users = User.objects.all()

    def create_ratings(self):
        items = []
        self.rating_total = []
        self.rating_count = 200
        for i in range(0, self.rating_count):
            user_obj = self.users.order_by("?").first()
            ply_obj = self.playlists.order_by("?").first()
            rating_val = random.choice(RatingChoices.choices)[0]
            if rating_val is not None:
                self.rating_total.append(rating_val)
            items.append(
                Rating(
                    user=user_obj,
                    content_object=ply_obj,
                    value=rating_val
                )
            )
        Rating.objects.bulk_create(items)
        self.ratings = Rating.objects.all()

    def setUp(self):
        self.create_playlists()
        self.create_users()
        self.create_ratings()

    def test_user_count(self):
        qs = User.objects.all()
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.user_count)
        self.assertEqual(self.users.count(), self.user_count)

    def test_playlist_count(self):
        qs = Playlist.objects.all()
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.playlist_count)
        self.assertEqual(self.playlists.count(), self.playlist_count)

    def test_rating_count(self):
        qs = Rating.objects.all()
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.rating_count)
        self.assertEqual(self.ratings.count(), self.rating_count)

    def test_rating_random_choices(self):
        value_set = set(Rating.objects.values_list('value', flat=True))
        self.assertTrue(len(value_set) > 1)

    def test_rating_aggregate(self):
        db_avg = Rating.objects.aggregate(average=Avg('value'))['average']
        self.assertIsNotNone(db_avg)
        self.assertTrue(db_avg > 0)
        total_sum_of_ratings = sum(self.rating_total)
        result_avg = total_sum_of_ratings / (len(self.rating_total) * 1.0)  # * 1.0 for float value
        self.assertEqual(result_avg, db_avg)

    def test_rating_playlist_aggregate(self):
        item_1 = Playlist.objects.aggregate(average=Avg('ratings__value'))['average']
        self.assertIsNotNone(item_1)
        self.assertTrue(item_1 > 0)
