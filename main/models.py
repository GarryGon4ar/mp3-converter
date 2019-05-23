from django.db import models



class Song(models.Model):
    link = models.URLField(max_length=250)