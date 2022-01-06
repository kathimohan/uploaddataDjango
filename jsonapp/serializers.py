from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import *
from rest_framework.authtoken.models import Token
from rest_framework_tricks.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)
class jsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = jsondata
        fields = ['id', 'userId', 'title', 'body']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
