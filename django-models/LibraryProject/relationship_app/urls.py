from django.urls import path
from .views import book_list_view

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),  # URL for the function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
]
