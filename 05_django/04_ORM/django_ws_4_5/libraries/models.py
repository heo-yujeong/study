from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        TTBKey = ''
        url = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType=ItemNewAll&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101'
        response = requests.get(url)
        data = response.json()
        cat = data['searchCategoryName']
        cat_id = data['searchCategoryId']

        for item in data['item']:
            book = Book(isbn=item['isbn'], author=item['author'], title=item['title'],
                       category_name=cat, category_id=cat_id,
                       price=item['priceSales'], fixed_price=item['fixedPrice'], pub_date=item['pubDate'])
            book.save()