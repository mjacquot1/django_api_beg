from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serilizes a name field for testing out the API view"""
    name = serializers.CharField(max_length=10)
    car = serializers.CharField(max_length=10)


class GoodbyeSerializer(serializers.Serializer):
    """Serilizes a name field for testing out the API view"""
    date = serializers.CharField(max_length=10)
    age = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialized a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(selfe, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
