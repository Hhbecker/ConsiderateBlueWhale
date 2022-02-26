from django.forms import ModelForm

from .models import AudioFile

# forms turn model fields into prompts with the same requirements that are set in the model
# for example: the AudioFile model has a title field with max length of 200 characters so the 
# form creates a text input box with a max length of 200 characters

# What kind of model is this? there are two kinds in the django docs 


class AudioFileForm(ModelForm):
    # what is class Meta?
    class Meta:
        model = AudioFile
        # change __all__ to all expect bpm b/c this is calculated within view
        fields = '__all__'