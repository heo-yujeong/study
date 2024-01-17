import requests
from pprint import pprint as print

dummy_data = []
for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data)