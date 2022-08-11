from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    postslug = models.SlugField(blank=True, null=True)
    spaceslug = models.CharField(max_length=100, blank=True, null=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.post_slug is None:
            self.post_slug = "post-" + slugify(self.title)
        super().save(*args, **kwargs)
     
    class Meta:
        ordering = ['-date_added']