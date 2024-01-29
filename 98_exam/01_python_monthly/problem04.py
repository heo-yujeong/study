############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = False # 비밀번호의 길이 수가 비정상 or 비밀번호와 확인란의 값이 다르다고 가정
    len_u_pw = 0 # 비밀번호의 길이를 저장할 변수
    for _ in user.get('password'): # 비밀번호를 모두 순회하는 동안
        len_u_pw += 1 # 비밀번호의 길이를 + 1
    if 8 <= len_u_pw < 32 and user.get('password') == user.get('password_confirm'):
        # 비밀번호의 길이가 8자리 이상, 32자리 미만이고, 비밀번호와 확인란의 값이 같으면
        result = True # 정상범위 + 값이 일치한다고 반환
        
    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
