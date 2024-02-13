import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 후위표기법 수식
    postfix = input().split()

    stack = []
    # 결과는 error로 초기화
    # 연산이 가능하다면 그 때 result값을 연산 결과로
    result = 'error'

    # 수식을 모두 순회하면서
    for token in postfix:
        # token이 수식의 종료를 알리는 .이고, 그때 stack이 비어있지 않으면
        if token == '.' and stack:
            # .이 나왔지만 stack의 길이가 2 이상이면 형식이 잘못됨
            if len(stack) >= 2:
                break
            # stack의 길이가 1일 때 result의 값에 할당
            else:
                result = stack.pop()

        # token이 연산자이면
        elif token in '+-*/':
            # stack에 2개 이상의 요소가 있으면
            if len(stack) >= 2:
                # 2개의 수를 해당하는 연산자에 맞춰 연산 후 다시 stack에 append
                # 먼저 pop되는 수를 뒤에서 연산해야 하기 때문에 2번부터 받음
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 // num2)
            # 연산자가 들어왔지만 stack에 2개 이상의 요소가 없다면 연산 불가
            else:
                break
        # token이 정수이면
        else:
            # 이후 연산을 해주기 위해 int형으로 형변환 하여 stack에 append
            stack.append(int(token))

    print(f'#{test_case} {result}')