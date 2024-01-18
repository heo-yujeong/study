# 함수 정의
def some_func(parm1, parm2): # 2개의 매개변수를 가진다
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2    

# 함수 호출
some_func(3, 1)
some_func(3, 1.1)
some_func('가', '나')

# 함수 호출한 결과를 어떤 변수에 할당
answer = some_func(1, 2)
print(answer) # None => 값이 없음 => 함수의 output이 없기 때문


def some_func2(parm1, parm2):
    result = parm1 + parm2
    return result

answer2 = some_func2(1, 2)
print(answer2) # 3


# 문) number를 오름차순으로 정렬
numbers = [4, 3, 2, 1]
# 메서드 : 누군가가 가지고 있는 함수 => 함수니까 사용방법은 동일!
# 리스트가 가진 sort() => 정렬 대상인 리스트가 정해져있다
# reverse=True 인자 추가하면 내림차순으로 정렬
result = numbers.sort()
print(result) # None => 함수는 실행되었지만 return값이 없음!
print(numbers) # [1, 2, 3, 4] => 출력해보면 sort()는 본인의 할일(오름차순 정렬)을 했다는 것을 알 수 있음

# 내장함수 : 파이썬이 기본적으로 가지고 있는 함수
# sorted() => 누구를 정렬할 것인지 인자를 넘겨줘야 한다
# 넘겨받은 인자는 수정하지 않음
numbers = [4, 3, 2, 1]
result2 = sorted(numbers)
print(result2)
print(numbers)



def other_func(parm1, parm2):
    result = parm1 * parm2
    print(result, '함수 내부에서 실행')
    return result

answer3 = other_func(2, 3)
print(answer3, '함수 외부에서 실행')


'''
함수를 만드는 이유? 똑같은 코드를 다시 쓰지 말자!
for문이 반복문 아닌가? 단순히 코드의 반복이 아닌,
input에 따라 output이 달라지는 모든 경우에 대입하기 위한 것!
'''