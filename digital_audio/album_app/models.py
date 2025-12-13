from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Image(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='images'
    )
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='albums/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
