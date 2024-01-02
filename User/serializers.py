#serialzer for ruser
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = rUser
        fields = ('user_id', 'user_name', 'user_email', 'user_password', 'user_phone','user_country')
        extra_kwargs = {'user_password': {'write_only': True}}
    def create(self, validated_data):
        user = rUser.objects.create_user(**validated_data)
        return user