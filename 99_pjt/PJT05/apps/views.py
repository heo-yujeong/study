from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver

from .models import Article, Query

def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    g_list = soup.select('div.g')
    result = []
    for g in g_list:
        title = g.select_one('.LC20lb.MBeuO.DKV0Md')
        if title is not None:
            result.append(title.text)
    return result


# Create your views here.
def crawling(request):
    keyword = '탕수육'
    titles = get_data(keyword)
    for title in titles:
        article, created_article = Article.objects.get_or_create(title=title)
        query_obj, created_query = Query.objects.get_or_create(article=article, keyword=keyword)
    return 