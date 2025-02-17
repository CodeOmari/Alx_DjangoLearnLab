from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic.detail import DetailView
# Create your views here.

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['books'] = self.object.books.all()
       return context