## creating an object instance in the model Book

book_instance = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

## Retrieve all records from the database model

from bookshelf.models import Book

retrieve = Book.objects.all()

print(retrieve)

<QuerySet [<Book: Book object (1)>]>


## Updating records in your models

update_record = Book.objects.update(title="Nineteen Eighty-Four")

retrieve_books = Book.objects.all()

<QuerySet [<Book: Book object (1)>]>


## Deleting records in a model

from bookshelf.models import Book

Book.objects.all().delete()