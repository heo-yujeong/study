number_of_people = 0


def increase_user(number_of_people):
    return number_of_people + 1


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    return {'name' : name, 'age' : age, 'address' : address}

user_info ={}
print(number_of_people)
create_user('홍길동', 30, '서울')