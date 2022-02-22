from django.db import models
from django.forms import IntegerField

# Create your models here.

class AudioFile(models.Model):
    title = models.CharField(max_length=200)
    length = models.TimeField()
    bpm = models.IntegerField()

    def __str__(self):
        return self.title