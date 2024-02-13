import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = []

    # 중위표현식 -> 후위표현식
    for token in infix:
        if token.isdecimal():
            postfix += token
        elif token == '*':
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(token)
        elif token == '+':
            while stack:
                postfix += stack.pop()
            stack.append(token)

    while stack:
        postfix += stack.pop()


    for token in postfix:
        if token in '+*':
            num1, num2 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(int(num1) + int(num2))
            else:
                stack.append(int(num1) * int(num2))
        else:
            stack.append(int(token))

    print(f'#{test_case} {stack.pop()}')