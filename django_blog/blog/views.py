from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm

# Create your views here.


# User Registration
# Import the UserCreationForm from django.contrib.auth.forms
# Import login from django.contrib.auth
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# User Login
# Django provides a built-in LoginView
# Import LoginView from django.contrib.auth.views
class UserLoginView(LoginView):
    template_name = 'blog/login.html'


# Logout
def signout_user(request):
    logout(request)
    return redirect('login')



def profile_view(request):
    """
    Allows authenticated users to view and edit their profile details.

    - Displays the profile form pre-filled with user details.
    - Handles form submission to update user details.
    - Redirects to the profile page with a success message upon update.

    Arguments:
    request -- HTTP request object.
    """
    if request.method == 'POST':
        # Populate form with POST data and the authenticated user instance
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # Pre-fill the form with current user data
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})
