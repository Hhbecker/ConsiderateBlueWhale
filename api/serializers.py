# Tbh im confused about serializers (it works without them idk what they do)

# When a user submits information (such as creating a new instance) through 
# the API, the serializer takes the data, validates it, and converts it into 
# something Django can slot into a Model instance. Similarly, when a user 
# accesses information via the API the relevant instances are fed into the 
# serializer, which parses them into a format that can easily be fed out as 
# JSON to the user.


from rest_framework import serializers
# import your model 
from .models import AudioFile

# Serializer for AudioFile model
class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        # determines which fields should be handled (converted) by the serializer
        fields = '__all__'