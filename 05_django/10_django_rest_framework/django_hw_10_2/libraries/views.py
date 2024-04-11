from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BookListSerializer, BookSerializer
from .models import Book

# Create your views here.
@api_view(['GET'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)