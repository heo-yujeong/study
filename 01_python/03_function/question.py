'''
함수를 정의할 때, 매개변수에 패킹을 사용해서 가변인자로 받게 되면 튜플로 받는데
왜, 변수에 패킹을 사용해서 다수의 데이터를 받으면 리스트로 받는 이유는?

tuple
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable한 데이터
- 여러 개의 데이터를 담을 수 있는 collection
- 내부 요소를 변경 할 수 없는 immutable

list
- 순서가 있는 시퀀스 타입
- 순회가 가능한 iterable한 데이터
- 여러 개의 데이터를 담을 수 있는 collection
- 내부 요소를 변경 할 수 있는 mutable
'''

def some_func(*args):
    print(args)
    print(type(args))

some_func(1, 2, 3, 4)

a, *b, c = [1, 2, 3, 4, 5]
print(b)
print(type(b))

'''
변수에 값을 할당할 때 기대값은
- 특정 데이터를 편하게 참조할 수 있는 기능
- 해당 데이터의 값을 변경하거나, 조작하거나, 활용하는 용도를 기대

함수는 입력 값에 따른 정확한 출력 값을 기대
- 함수가 하는 일에 대해 항상 같은 입력 값에 같은 출력 값이 나와야 함
'''

print([1, 2, 3, 4, 5])
print(*[1, 2, 3, 4, 5])


'''
함수
- 입력에 대한 출력이 있다!

기명함수
def 함수이름(매개변수):
    함수가 할일
- 코드재사용 가능
- 이름이 있어서 나중에 다시 부를 수 있음

익명함수
lambda(매개변수 : 함수가 할일)
- 코드 재사용 불가능
- 순회가능한 어떤 데이터에 대해 각 요소들에 대해서만 똑같은 로직 실행해야 할 때(일회성. 간단한 로직)
'''
def my_sum(num1, num2):
    return num1 + num2

result = my_sum(1, 2)
print(result)

my_sum_lambda = lambda num1, num2 : num1 + num2
result2 = my_sum_lambda(1, 2)
print(result2)

a = [1, 2, 3]
b = [4, 5, 6]
result3 = map(lambda num1, num2 : num1 + num2, a, b)
print(list(result3))

result4 = map(my_sum, a, b)
print(list(result4))