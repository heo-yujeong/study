from rest_framework import serializers
from .models import Location, Station

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class StationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('address', 'is_opening',)

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address',)

class StationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'