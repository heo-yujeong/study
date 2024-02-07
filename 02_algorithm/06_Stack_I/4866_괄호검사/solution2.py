import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    code = input()
    stack = [0] * len(code)
    top = -1
    result = 0

    for char in code:
        if char in '{(':
            top += 1
            stack[top] = char
        elif char in '})':
            if top != -1 and ((stack[top] == '{' and char == '}') or (stack[top] == '(' and char == ')')):
                stack[top] = 0
                top -= 1
            else:
                break

    else:
        if top == -1:
            result = 1

    print(f'#{test_case} {result}')