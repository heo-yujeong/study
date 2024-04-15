from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )


class ReviewListSerializer(serializers.ModelSerializer):
    class BookIsbnSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)
    
    book = BookIsbnSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

class BookSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)