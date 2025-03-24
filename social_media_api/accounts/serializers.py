from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

# Dynamically get the user model
CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    # The password is defined as write-only
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = '__all__'


    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
        )
        # Automatically create a token for the newly created user
        Token.objects.create(user=user)
        return user