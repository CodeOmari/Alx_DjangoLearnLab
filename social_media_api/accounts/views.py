from django.shortcuts import render
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView # Allows you to handle HTTP request
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