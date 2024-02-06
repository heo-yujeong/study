import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    code = input()

    stack = []
    result = 0

    for char in code:
        if char in '{(':
            stack.append(char)
        elif char in '})':
            if stack and ((stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')')):
                stack.pop()
            else:
                break

    else:
        if not stack:
            result = 1

    print(f'#{test_case} {result}')