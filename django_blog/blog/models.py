from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, help_text="A short bio about yourself.")

    # Add related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Set a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Set a unique related_name
        blank=True
    )



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Unique name for the tag
    

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True) 

    def __str__(self):
        return self.title

    
    class Meta:
        db_table = 'Post'



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

    class Meta:
        db_table = 'Comment'