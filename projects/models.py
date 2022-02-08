from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_es = models.CharField(max_length=200, unique=True, default=None)
    description = models.TextField()
    description_es = models.TextField(default=None)
    technology = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    link = models.URLField(max_length = 200, default=None, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='projects_images')
    def __str__(self):
        return self.title

# Create your models here.
