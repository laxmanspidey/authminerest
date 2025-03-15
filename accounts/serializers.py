# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         Token.objects.create(user=user)  # Create a token for the user
#         return user

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)  # Add confirm_password field

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'confirm_password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Passwords do not match.")
#         return data

#     def create(self, validated_data):
#         # Remove confirm_password from validated_data
#         validated_data.pop('confirm_password')
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         Token.objects.create(user=user)  # Create a token for the user
#         return user
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)  # Add confirm_password field

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Remove confirm_password from validated_data
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Create a token for the user
        return user