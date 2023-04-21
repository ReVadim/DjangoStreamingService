from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from src.playlists.mixins import PlaylistMixin
from src.playlists.models import Playlist
from src.tags.models import TaggedItem

from django.db.models.signals import pre_save


class TaggedItemView(View):
    """ Tags list view
    """
    def get(self, request):
        tag_list = TaggedItem.objects.unique_list()
        context = {
            'tag_list': tag_list
        }
        return render(request, 'tags/tag_list.html', context)


class TaggedItemDetailView(PlaylistMixin, ListView):
    """ Detail tags view
    """

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = f"{self.kwargs.get('tag')}".title()
        return context

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        return Playlist.objects.filter(tags__tag=tag).movie_or_show()


def lowercase_tag_pre_save(sender, instance, *args, **kwargs):
    instance.tag = f"{instance.tag}".lower()


pre_save.connect(lowercase_tag_pre_save, sender=TaggedItem)
