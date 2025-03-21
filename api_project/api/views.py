from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from rest_framework import IsAuthenticated

# Create your views here.

# Uses the serializer class to retrieve and return Book data
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer



# Handles all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]