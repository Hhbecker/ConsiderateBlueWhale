from asyncio import FastChildWatcher
from django.db import models
from django.forms import IntegerField
import librosa as lib
import pathlib

# Create your models here.

# model AudioFile: contains fields for a title (char) and bpm (int)
class AudioFile(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    bpm = models.IntegerField(null=True)
    # for audio files, specifies folder in server where uploaded files should be stored
    file = models.FileField(upload_to='audiofiles/', max_length=100, blank=False, null=False)

    # the toString method -> return the contents of the title field
    def __str__(self):
        return self.title

    @property
    def getBpm(self):
        print("\n\n\n Filename:" + self.file.name + " \n\n\n")
        y,sr = lib.load(self.file.name)
        # confirm input is valid audio file with positive duration
        if lib.util.valid_audio(y):
            #length = lib.get_duration(audioFile) 
            onset_env = lib.onset.onset_strength(y=y, sr=sr)
            tempo = lib.beat.tempo(onset_envelope=onset_env, sr=sr)
            return tempo[0]
        else:
            return 'error'

