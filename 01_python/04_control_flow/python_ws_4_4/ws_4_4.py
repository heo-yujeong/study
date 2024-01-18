import requests

dummy_data = []
for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()

    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dummy_data.append({'company': parsed_data['company']['name'], 'lat': parsed_data['address']['geo']['lat'], 'lng': parsed_data['address']['geo']['lng'], 'name': parsed_data['name']})
    

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

censored_user_list = {}

def create_user(dummy_list):
    for dummy in dummy_list:
        key = dummy['company']
        value = [dummy['name']]
        if censorship({key : value}):
            censored_user_list[key] = value

def censorship(user_dict):
    for user in user_dict:
        if user in black_list:
            print(f'{user} 소속의 {(user_dict[user])[0]} 은/는 등록할 수 없습니다.')
            return False
        else:
            print('이상 없습니다.')
            return True


create_user(dummy_data)
print(censored_user_list)