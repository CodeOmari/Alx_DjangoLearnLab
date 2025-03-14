## Retrieve all records from the database model

from bookshelf.models import Book

retrieve = Book.objects.get(title='1984')

print(retrieve)

<Book: 1984>