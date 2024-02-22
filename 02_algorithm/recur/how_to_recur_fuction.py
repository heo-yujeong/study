'''
위와 아래는 다른 형태이지만 같은 일을 하는 코드!

def 어떤일을 하는 함수():
    if 이 조건을 만족한다면:
        return 특정 값 반환
    elif 만족하지 못한다면:
        어떤 일을 수행
        어떤일을 하는 함수()


while 이 조건을 만족하는 동안:
    어떤 일을 수행

'''
def sum(a, b):
    return a + b
def other():
    return sum(3, 4)

result = other()
print(result)


def some(N):
    if N == 0:
        return 1
    else:
        N -= 1
        print(N)
        return some(N)

result2 = some(10)
print(result2)