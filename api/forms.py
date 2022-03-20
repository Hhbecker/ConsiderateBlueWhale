# Contains form to turn model fields into prompts displayable in html

from django.forms import ModelForm

from .models import AudioFile

# forms turn model fields into prompts with the same requirements that are set in the model
# for example: the AudioFile model has a title field with max length of 200 characters so the 
# form creates a text input box with a max length of 200 characters

# What is the significance of passing in ModelForm?

class AudioFileForm(ModelForm):
    # what is class Meta?
    class Meta:
        model = AudioFile
        # include all fields except bpm in the form
        fields = ['title', 'artist', 'file']