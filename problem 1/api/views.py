from django.shortcuts import render

# Create your v# your_app_name/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_tenants.utils import set_tenant
from .models import User, Tenant
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Extract tenant information from request or use default
        tenant = request.data.get('tenant', 'default_tenant')

        # Ensure that the tenant exists
        if not Tenant.objects.filter(schema_name=tenant).exists():
            return Response({'message': 'Invalid tenant'}, status=status.HTTP_400_BAD_REQUEST)

        # Switch to the tenant's schema
        set_tenant(Tenant.objects.get(schema_name=tenant))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Return to the default schema
        set_tenant(None)  # Set to None to revert to the default schema

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
