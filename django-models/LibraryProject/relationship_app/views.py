from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def book_list_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['books'] = self.object.books.all()
       return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # automatically logins the user after registration
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form':form})

# Login view using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Admin view (Only accessible by Admin users)
@user_passes_test(Admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# Helper function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


# Admin View (Accessible by Admin users only)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Librarian View (Accessible by Librarian users only)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Member View (Accessible by Member users only)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')