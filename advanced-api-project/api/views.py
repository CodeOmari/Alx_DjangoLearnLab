from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from api.models import Book
from api.serializers import BookSerializer
from rest_framework import filters 
from rest_framework.filters import SearchFilter, OrderingFilterr
from django_filters import rest_framework 
from rest_framework import generics


# Create your views here.

# Listing all books in youe Book model
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


# Retrieve a specific book by ID
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Adding new book
# Authenticated users only can add a new book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAuthenticated]

# Updating book details
# Admin only can update a book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

# Delete a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAdminOrReadOnly]