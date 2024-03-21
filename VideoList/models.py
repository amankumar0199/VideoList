from django.db import models

# Create your models here.


class VideoList(models.Model):
    video_title = models.CharField(max_length=500)
    description = models.TextField()
    publishing_datetime = models.DateTimeField()
    thumbnails_URLs = models.URLField()
    objects = models.Manager()


