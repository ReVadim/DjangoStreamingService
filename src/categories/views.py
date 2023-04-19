from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import ListView
from src.playlists.models import Playlist
from src.categories.models import Category

from src.playlists.mixins import PlaylistMixin


class CategoryListView(ListView):
    """ Category model list view
    """
    queryset = Category.objects.all().filter(active=True)


class CategoryDetailView(PlaylistMixin, ListView):
    """ Another list view for Playlist categories
    """
    def get_context_data(self):
        context = super().get_context_data()
        try:
            obj = Category.objects.get(slug=self.kwargs.get('slug'))
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise Http404
        except:
            obj = None

        context['object'] = obj
        if obj is not None:
            context['title'] = obj.title

        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Playlist.objects.filter(category__slug=slug)
