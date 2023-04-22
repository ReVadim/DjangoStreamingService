from django.test import TestCase

from src.playlists.models import Playlist, TVShowProxy, MovieProxy


class PlaylistViewTestCase(TestCase):
    """ Playlist views Test Case
    """
    fixtures = ['projects']

    def test_queryset_exists(self):
        self.assertTrue(Playlist.objects.exists())

    def test_movie_count(self):
        qs = MovieProxy.objects.all()
        self.assertEqual(qs.count(), 5)

    def test_shows_count(self):
        qs = TVShowProxy.objects.all()
        self.assertEqual(qs.count(), 2)
    #
    def test_show_detail_view(self):
        show = TVShowProxy.objects.all().published().first()
        url = show.get_absolute_url()
        self.assertIsNotNone(url)
        response = self.client.get(url)  # GET request to some url
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"{show.title}")
        # html = response.content
        context = response.context
        obj = context['object']
        self.assertEqual(obj.id, show.id)

    def test_show_detail_redirect_view(self):
        show = TVShowProxy.objects.all().published().first()
        url = f"/shows/{show.slug}"
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_list_view(self):
        show_qs = TVShowProxy.objects.all().published()
        response = self.client.get("/shows/")
        self.assertEqual(response.status_code, 200)
        context = response.context
        response_queryset = context['object_list']
        self.assertQuerysetEqual(show_qs.order_by('-timestamp'), response_queryset.order_by('-timestamp'))

    def test_movie_detail_view(self):
        movie = MovieProxy.objects.all().published().first()
        url = movie.get_absolute_url()
        self.assertIsNotNone(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"{movie.title}")
        context = response.context
        obj = context['object']
        self.assertEqual(obj.id, movie.id)

    def test_movie_detail_redirect_view(self):
        movie = MovieProxy.objects.all().published().first()
        url = f"/movies/{movie.slug}"
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_movie_list_view(self):
        movie_qs = MovieProxy.objects.all().published()
        response = self.client.get("/movies/")
        self.assertEqual(response.status_code, 200)
        context = response.context
        response_qs = context['object_list']
        self.assertQuerysetEqual(movie_qs.order_by('-timestamp'), response_qs.order_by('-timestamp'))
