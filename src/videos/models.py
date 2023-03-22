from django.db import models


class Video(models.Model):
    """ Main Video model
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    @property
    def is_published(self):
        return self.active


class VideoAllProxy(Video):
    """ Proxy model that displays all videos
    """
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    """ Proxy model that displays only published videos
    """
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'
