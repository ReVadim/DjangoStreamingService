from  django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class TaggedItemManager(models.Manager):
    """ Tagged manager
    """
    def unique_list(self):
        tags_set = set(self.get_queryset().values_list('tag', flat=True))

        return sorted(list(tags_set))


class TaggedItem(models.Model):
    """ Tag model
    """
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    objects = TaggedItemManager()

    @property
    def slug(self):
        return self.tag
