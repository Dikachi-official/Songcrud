from django.db import models

# Create your models here.
class Song(models.Model):
  title = models.CharField(max_length=100)
  artiste = models.CharField(max_length=30)
  genre = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  
