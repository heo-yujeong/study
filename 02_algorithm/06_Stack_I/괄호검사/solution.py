import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    bracket = input()

    stack = []
    result = False

    for brac in bracket:
        if brac in ['(', '[', '{']:
            stack.append(brac)
        elif brac in [')', ']', '}']:
            if stack and ((stack[-1] == '(' and brac == ')') or (stack[-1] == '[' and brac == ']') or (stack[-1] == '{' and brac == '}')):
                top = stack.pop()
            else:
                break

    else:
        if not stack:
            result = True

    print(f'#{test_case} {result}')

