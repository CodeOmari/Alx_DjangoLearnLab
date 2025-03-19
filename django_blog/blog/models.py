from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, help_text="A short bio about yourself.")



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Unique name for the tag
    

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    
    class Meta:
        db_table = 'Post'