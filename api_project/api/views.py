from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from api.models import Book

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer