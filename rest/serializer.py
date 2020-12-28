from rest_framework import serializers
from rest.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',
               'age',
               'location')
