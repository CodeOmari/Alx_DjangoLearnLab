## Deleting records in a model

from bookshelf.models import Book

book.delete()

## Confirm if the records are deleted

Book.objects.all()

<QuerySet []>