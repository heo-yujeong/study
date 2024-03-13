import requests
import pprint

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
book_list = response['item']

result = []
for i in range(len(book_list)):
    result.append({'국제 표준 도서 번호': book_list[i]['isbn'],
                   '저자': book_list[i]['author'],
                   '제목': book_list[i]['title'],
                   '출간일': book_list[i]['pubDate']})
pprint.pprint(result)