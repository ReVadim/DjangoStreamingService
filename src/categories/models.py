from django.db import models


class Category(models.Model):
    """ Category model
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Category (id={self.id}) - {self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
