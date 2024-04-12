import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/tag/love/'

response = requests.get(url)
html_text = response.text
# print(html_text) # str type

soup = BeautifulSoup(html_text, 'html.parser')
# print(soup)

# 1. find
main = soup.find('a')
# print(main) # a 태그 전체가 출력
# print(main.text) # a 태그가 가진 요소 출력

# 2. find_all
a_tags = soup.find_all('a')
# print(a_tags) # 리스트로 반환

# 3. select_one
word = soup.select_one('.text')
# print(word.text)

# 4. select
words = soup.select('.text')
for w in words:
    print(w.text)