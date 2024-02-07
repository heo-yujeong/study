import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):
    code = input()

    # 여는 괄호 ( or {이 들어오면 stack에 넣고,
    # (스택이 비어있지 않은 경우)
    # 닫는 괄호 ) or }이 들어오면 가장 위에 있는 원소가 같은 짝인지 확인 후
    # 짝이 맞다면 pop해서 없애줌
    stack = []
    # 괄호가 제대로 있는지 아닌지 확인
    result = 0

    for char in code:
        if char in '{(':
            stack.append(char)
        elif char in '})':
            if stack and ((stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')')):
                stack.pop()
            else:
                break

    # 코드를 모두 순회한 후에 스택이 비어 있으면 괄호가 맞게 들어 있는 것!
    else:
        if not stack:
            result = 1

    print(f'#{test_case} {result}')