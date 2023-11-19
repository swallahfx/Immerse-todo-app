from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        # Use set_password to hash the user's password
        user.set_password(self.request.data['password'])
        user.save()

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user:
            # Generate refresh and access tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            access_token_expiry = datetime.utcfromtimestamp(access_token['exp']).strftime('%Y-%m-%d %H:%M:%S')

            # Include additional user data in the response
            serializer = UserSerializer(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(access_token),
                    "expiry": access_token_expiry

                    # "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TokenRefreshView(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Attempt to refresh the access token using the provided refresh token
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            
            # Include the new access token in the response
            return Response({"access": new_access_token}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": f"Failed to refresh access token. {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


