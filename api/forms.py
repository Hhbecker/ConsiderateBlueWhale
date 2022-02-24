from django.forms import ModelForm

from .models import AudioFile

class AudioFileForm(ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'