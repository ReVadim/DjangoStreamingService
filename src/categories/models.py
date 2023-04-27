from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import pre_save

from src.tags.models import TaggedItem

from src.djangoflix.db.receivers import unique_slugify_pre_save


class Category(models.Model):
    """ Category model
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = GenericRelation(TaggedItem, related_query_name='category')

    def __str__(self):
        return f'Category (id={self.id}) - {self.title}'

    def get_absolute_url(self):
        return f"/category/{self.slug}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


pre_save.connect(unique_slugify_pre_save, sender=Category)
