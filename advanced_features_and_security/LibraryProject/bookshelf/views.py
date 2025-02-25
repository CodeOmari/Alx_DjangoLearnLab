from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from .forms import ExampleForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')





@permission_required('myapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('myapp.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        # Handle book creation logic
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book created successfully")
    return render(request, 'bookshelf/book_form.html')

@permission_required('myapp.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Handle book update logic
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated successfully")
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('myapp.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted successfully")




def search_books(request):
    # Sanitize input using forms
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        # Use Django ORM to prevent SQL injection
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


def add_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your book list view name
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})