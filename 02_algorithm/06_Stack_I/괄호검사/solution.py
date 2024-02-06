import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    bracket = input()

    stack = []

    for brac in bracket:
        if brac in ['(', '[', '{']:
            stack.append(brac)
        elif brac in [')', ']', '}']:
            if stack:
                top = stack.pop()
                if (top == '(' and brac == ')') or (top == '[' and brac == ']') or (top == '{' and brac == '}'):
                    continue
                else:
                    print('괄호가 맞지 않음')
                    break
        else:
            continue

    if stack:
        print('괄호 개수가 다름')
    else:
        print('괄호 검사 완료!')

