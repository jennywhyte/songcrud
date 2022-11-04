from rest_framework import serializers
from . models import *

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Artiste
        fields = '_all_'


class SongSerializer(serializers.ModelSerializer):
    class Meta():
        model = Song
        fields = '_all_'

class LyricSerializer(serializers.ModelSerializer):
    class Meta():
        model = Lyric
        fields = '_all_'

