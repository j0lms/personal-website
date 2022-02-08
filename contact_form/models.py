from django.db import models
from django.utils import timezone

class Message(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)

# Create your models here.
