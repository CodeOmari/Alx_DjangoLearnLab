from django.urls import path,include
from api.views import BookList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'books_all', BookViewSet, basename= 'book_all')
urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
]