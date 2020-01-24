# serializers.py
from rest_framework import serializers

from .models import DistrictDate

class DistrictDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DistrictDate
        fields = ('district', 'number')