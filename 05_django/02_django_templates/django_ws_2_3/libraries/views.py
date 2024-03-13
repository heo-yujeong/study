from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = ''
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': 50,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()
    book_list = response.get('item')

    books = []
    for i in range(len(book_list)):
        books.append((book_list[i].get('title'), book_list[i].get('author'), book_list[i].get('pubDate'), book_list[i].get('isbn')))
    context = {
        'books': books
    }
    return render(request, 'recommend.html', context)





