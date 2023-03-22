from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllAdmin(admin.ModelAdmin):
    """ Admin model class Video
    """
    list_display = ['title', 'id', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id', 'is_published']

    # def published(self, obj, *args, **kwargs):
    #     return obj.active

    class Meta:
        model = VideoAllProxy


admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    """ Admin model class Video
    """
    list_display = ['title', 'video_id']
    search_fields = ['title']

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

    class Meta:
        model = VideoPublishedProxy


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
