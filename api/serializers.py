from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'code', 'NameWoDiacritics', ]
