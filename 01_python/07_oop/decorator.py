def my_decorator(func):
    def wrapper():
        print('인자로 받은 func 호출되기 전에 할 일')
        func()
        print('인자로 받은 func 호출되고 나서 할 일')
    return wrapper

@my_decorator
def greeting():
    print('안녕~')


greeting()