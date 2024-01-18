# 단축평가
one = 3
two = 0
print(one or two) # 단축평가 => two라는 값이 무엇인지 알 필요가 없다!
if one or two:
    print('or 연산 통과')
else:
    print('or 연산 통과 못함')


# 암시적 형변환
print(0 == False) # true
print(-1 == False) # false
print('' == False) # false
print('' == True) # false

if '':
    print('빈 문자열은... 빈 문자열...?')
else:
    print('아무일도 벌어지지 않음')

three = '' # false로 암시적 형변환
four = '4'
if three and four: # => if '': 와 같음
    print('3과 4')
else:
    print('실패')


if one % 2: # 익숙해지면 이렇게 쓰기도!
    print('홀수')