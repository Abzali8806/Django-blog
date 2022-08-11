from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Space(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True)
    rules = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = "space-" + slugify(self.title)
        super().save(*args, **kwargs)