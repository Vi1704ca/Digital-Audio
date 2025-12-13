from django.db import models
from django.urls import reverse

# Create your models here.
class Songs(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    albom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('play_song', kwargs={'song_id': self.id})

    
