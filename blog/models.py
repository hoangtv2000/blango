from django.db import models
from django.conf import settings
# Create your models here.

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
   
    title = models.TextField(max_length=100)

    """A slug is a short string designed to be used as an identifier, such as in a URL. 
      Normally it is composed of lower case letters, numbers, and dashes. 
      Slugs are used for search engine optimization (making pages rank higher in search
      engine results), as well as to make URLs more readable for humans.
    """
    slug = models.SlugField()
    
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title