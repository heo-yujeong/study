number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    return {'name': name, 'age': age, 'address': address}


many_user = list(map(create_user, name, age, address))

def decrease_book(number_of_rent):
    global number_of_book
    number_of_book -= number_of_rent
    print(f'남은 책의 수 : {number_of_book}')

def rental_book(info):
    for key, value in info.items():
        us_name = key
        us_age = value
    decrease_book(us_age // 10)
    print(f'{us_name}님이 {us_age // 10}권의 책을 대여하였습니다.')


user_info = list(map(lambda x: {x['name'] : x['age']}, many_user))
list(map(rental_book, user_info))