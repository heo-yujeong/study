import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 동적인 페이지는 정상적으로 가져올 수 없음
    # response = requests.get(url)
    # print(response.text)

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    result_stats = soup.select_one('#result-stats')
    print(result_stats.text)

keyword = '탕수육'
get_data(keyword)