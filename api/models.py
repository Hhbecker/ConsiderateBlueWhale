from django.db import models
from django.forms import IntegerField

# Create your models here.

# model AudioFile: contains fields for a title (char) and bpm (int)
class AudioFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField()
    bpm = models.IntegerField()

    # the toString method -> return the contents of the title field
    def __str__(self):
        return self.title