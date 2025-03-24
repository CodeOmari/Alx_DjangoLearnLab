from django.shortcuts import render
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView # Allows you to handle HTTP request
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import CustomUser
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Token creation handled in the serializer
            return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token = user.auth_token.key  # Token directly retrieved
            user_data = CustomUserSerializer(user).data
            return Response({"token": token, "user": user_data}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class FollowUserView(generics.GenericAPIView):
    """
    View for following a user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # Explicit usage of CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_to_follow = self.get_object()  # Fetch user by `pk` from URL
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)  # Add to the following list
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """
    View for unfollowing a user.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # Explicit usage of CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_to_unfollow = self.get_object()
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(user_to_unfollow)  # Remove from the following list
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)