from typing_extensions import Required
from rest_framework import serializers

from .models import UserProfile, UserLocation


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    location = UserLocation(Required = False)
    class Meta:
        model = UserProfile
        fields = '__all__'