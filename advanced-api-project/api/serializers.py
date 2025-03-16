from rest_framework import serializers
from api.models import Book, Author
from datetime import datetime


# Serializer on the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    # validation to ensure that publication year is not in the future
    def validate_publication_year(self,value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError("Publish year cannot be in the future")
        return value


# Serializer on the Author Model
# Includes a nested serializer for the books written by the author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'