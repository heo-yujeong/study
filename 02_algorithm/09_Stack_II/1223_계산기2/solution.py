import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    # 수식의 길이
    N = int(input())
    # 중위표현식
    infix = input()
    # 후위표현식 저장할 문자열
    postfix = ''
    stack = []

    # 중위표현식 -> 후위표현식
    for token in infix:
        # 정수이면
        if token.isdecimal():
            postfix += token
        # * 이면
        elif token == '*':
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(token)
        # + 이면
        elif token == '+':
            while stack:
                postfix += stack.pop()
            stack.append(token)

    # 순회가 끝난 후 남아있는 연산자를 모두 후위표현식에 더함
    while stack:
        postfix += stack.pop()


    # 후위표현식에서 요소를 하나씩 꺼내면서 계산
    for token in postfix:
        # 연산자이면
        if token in '+*':
            # +, *는 숫자 순서 상관이 없기 때문에
            # 숫자 두개를 꺼내 연산 후 다시 append
            num1, num2 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(int(num1) + int(num2))
            else:
                stack.append(int(num1) * int(num2))
        # 정수이면
        else:
            stack.append(int(token))

    print(f'#{test_case} {stack.pop()}')