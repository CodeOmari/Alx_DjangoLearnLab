from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy

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




# View to display a list of all blog posts.
class PostListView(ListView):
    """
    A view that lists all the blog posts.
    
    Inherits from ListView. This view retrieves all the posts from the 
    database and renders them in a template. It uses the 'blog/post_list.html' 
    template and passes the list of posts to the template under the context name 'posts'.
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'  # Context name for the list of posts in the template.

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.all()


    

# View to display a single post with detailed information.
class PostDetailView(DetailView):
    """
    A view to display a detailed view of a single blog post.
    
    Inherits from DetailView. This view retrieves a single blog post based on its primary key 
    and renders it using the 'blog/post_detail.html' template. The post object is passed to the 
    template under the context name 'post'.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'  # Context name for the post object in the template.



# View to handle the creation of a new blog post.
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    A view for authenticated users to create a new blog post.
    
    Inherits from CreateView and requires the user to be logged in (LoginRequiredMixin).
    The form includes fields for the title and content of the post. Upon successful form submission, 
    the author is automatically set to the logged-in user. The user is redirected to the post list 
    upon successful creation.
    """
    model = Post
    fields = ['title', 'content', 'tags']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list view after successful creation.

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Process tags and associate them with the post
        tags = form.cleaned_data['tags']
        if tags:
            tag_names = {tag.strip() for tag in tags.split(',') if tag.strip()}  # Ensure no duplicates
            tags_objects = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]
            form.instance.tags.set(tags_objects)  # Associate the tags with the post
        return super().form_valid(form)



# View to handle the update/edit of an existing blog post.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view for authenticated users (who are the post authors) to update an existing blog post.
    
    Inherits from UpdateView and requires the user to be logged in (LoginRequiredMixin) and to be the 
    author of the post (UserPassesTestMixin). This view allows users to modify the title and content 
    of the post. Upon successful form submission, the user is redirected to the updated post's detail page.
    """
    model = Post
    fields = ['title', 'content', 'tags']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        """
        This method dynamically returns the URL for the updated post using its primary key (pk).
        This ensures that the user is redirected to the post's detail page after successfully updating it.
        """
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Process tags and associate them with the post
        tags = form.cleaned_data['tags']
        if tags:
            tag_names = {tag.strip() for tag in tags.split(',') if tag.strip()}  # Ensure no duplicates
            tags_objects = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]
            form.instance.tags.set(tags_objects)  # Update the post with the new tags
        return super().form_valid(form)

    def test_func(self):
        """
        This method checks whether the current user is the author of the post.
        It returns True if the user is the author, allowing them to edit the post.
        """
        post = self.get_object()
        return self.request.user == post.author



# View to handle the deletion of an existing blog post.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view for authenticated users (who are the post authors) to delete a blog post.
    
    Inherits from DeleteView and requires the user to be logged in (LoginRequiredMixin) and to be the 
    author of the post (UserPassesTestMixin). This view allows the author to delete their post. Upon successful 
    deletion, the user is redirected to the homepage.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')  # Redirect to the homepage after successful deletion.

    def test_func(self):
        """
        This method checks whether the current user is the author of the post.
        It returns True if the user is the author, allowing them to delete the post.
        """
        post = self.get_object()
        return self.request.user == post.author
