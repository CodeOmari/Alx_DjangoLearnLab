from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
<<<<<<< HEAD

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
=======
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
>>>>>>> e799462a14c80d8f7b8b682c8645cf58bb086db5
=======

>>>>>>> f9a5517f3e250d42b3390ede79299f6e02272228
