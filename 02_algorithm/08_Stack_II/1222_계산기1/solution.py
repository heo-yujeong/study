import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''

    stack = []

    for token in infix:
        if token in str(list(range(10))):
            postfix += token
        else:
            if not stack:
                stack.append(token)
            else:
                postfix += stack.pop()
                stack.append(token)
    else:
        postfix += stack.pop()

    result = 0

    for token in postfix:
        if token in str(list(range(10))):
            stack.append(token)
        else:
            num1, num2 = stack.pop(), stack.pop()
            stack.append(int(num1) + int(num2))

    result = stack.pop()

    print(f'#{test_case} {result}')