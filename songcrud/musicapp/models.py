from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    song_img_url = models.CharField(max_length=2000, default='', blank=True)

    def __str__(self):
        if self.title:
            return f'[Song title: {self.title}] [likes: {self.likes}]'
        return self.title



class Lyric(models.Model):
    content = models.CharField(max_length=4000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        if self.song_id:
            return f'{self.song_id}'
        return self.song_id

