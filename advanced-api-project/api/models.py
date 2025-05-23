from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Author'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    class Meta:
        db_table='Book'