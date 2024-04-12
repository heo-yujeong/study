import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    g_list = soup.select('div.g')
    for g in g_list:
        # LC20lb MBeuO DKV0Md
        title = g.select_one('.LC20lb.MBeuO.DKV0Md')
        if title is not None:
            print(title.text)

keyword = '탕수육'
get_data(keyword)