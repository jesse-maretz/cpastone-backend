from rest_framework import serializers
from .models import Footprint

class FootprintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Footprint 
        fields = ('date', 'footprint')