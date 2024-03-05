# your_app_name/serializers.py

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password', 'tenant')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        # Validate email format
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        return value

    def validate_phone_number(self, value):
        # Validate phone number format
 
        pattern = re.compile(r'^[0-9\s\+\(\)-]+$')
        if not pattern.match(value):
            raise serializers.ValidationError("Invalid phone number format.")
        return value

    def validate_password(self, value):
        # Validate password using Django's built-in validators
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value
