import requests
import pprint

api_key = '500f6bdb14771442cf9814c0110e6f33'

lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
pprint.pprint(data)
pprint.pprint(data['weather'])
pprint.pprint(data['weather'][0]['description'])
pprint.pprint(data.get('weather')[0].get('description'))


# 추가 공부 과제
# data['weather']와 data.get('weather')의 차이점?