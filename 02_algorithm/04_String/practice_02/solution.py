# str()함수를 사용하지 않고, itoa()를 구현
# 양의 정수를 입력받아 문자열로 변환하는 함수
# 입력 값 : 변환할 정수 값, 변환돈 문자열을 저장할 문자배열
# 반환 값 : 없음
# + 음수를 변환할 때는 어떤 고려 사항 필요?

def itoa(a):
    s = ''
    while a > 0:
        s = chr(a % 10 + ord('0')) + s
        a //= 10
    return s

ans = itoa(123)
print(ans)
print(type(ans))