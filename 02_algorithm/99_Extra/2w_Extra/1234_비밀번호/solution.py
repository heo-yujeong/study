import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11): # 10번의 테스트
    # N: 문자 길이, num_list: 소거 전 비밀번호
    N, num_list = input().split()

    # 비밀번호 담을 리스트(스택)
    pw_stack = []

    # 소거 전 비밀번호를 끝까지 순회하면서
    for num in num_list:
        # 비밀번호 스택에 요소가 있고,
        if pw_stack:
            # 이번에 들어온 문자가 스택의 가장 마지막 요소가 같으면
            if num == pw_stack[-1]:
                # 소거한다 = 스택에서 뺀다
                pw_stack.pop()
            # 다르다면
            else:
                # 스택에 추가한다.
                pw_stack.append(num)
        # 스택에 아무런 문자가 없을 때도 문자 추가
        else:
            pw_stack.append(num)

    # 비밀번호는 공백 없이 이어져 있기 때문에 공백 없이 출력
    pw = ''.join(pw_stack)

    print(f'#{test_case}', ''.join(pw_stack))