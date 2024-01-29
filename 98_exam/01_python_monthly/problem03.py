############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def check_user_id(user):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = False # 아이디의 길이가 모두 정상이 아니라고 가정
    len_u_id = 0 # 아이디의 길이를 저장할 변수
    for _ in user.get('user_id'): # 아이디를 모두 순회하는 동안
        len_u_id += 1 # 값이 있으면 길이 + 1
    if 4 <= len_u_id < 16: # 총 길이 수가 4글자 이상, 16글자 미만인지 확인(정상 범위인지 확인)
        result = True # 정상 범위이면 True

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
print(check_user_id(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_user_id(user_data2))  # False
#####################################################
