from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from api.models import Book

# Create your views here.
<<<<<<< HEAD

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
=======
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
>>>>>>> e799462a14c80d8f7b8b682c8645cf58bb086db5
