import sys
sys.stdin = open('input.txt')

isp = {'*' : 1, '+' : 0}    # 우선순위 값

for t in range(1, 11):
    N = int(input())    # 길이
    post = ''
    stack = []


    # 후위 표기법
    for i in input():
        if i.isdecimal():   # 숫자면
            post += i

        else:   # 아니면
            if not stack: # 스택이 비어있으면
                stack.append(i)

            elif isp[i] > isp[stack[-1]]:  # 우선순위가 스택의 마지막 값보다 크면 스택에 넣음
                stack.append(i)

            else:
                while stack and isp[i] <= isp[stack[-1]]:    # 스택이 비거나 우선 순위가 커질 때까지 반복
                    post += stack.pop()

                stack.append(i)   # + / * 밖에 없으니까 굳이 뺏다 넣었다 안해도 됌

    while stack:    # 스택에 남은 애들 정리
        post += stack.pop()

    print(post)
    # print(stack)

    # 계산
    for i in post:
        if i.isdecimal():   # 숫자면 int 형변환 해서 스택에 넣음
            stack.append(int(i))

        else:   # 아니면
            # +나 * 이니까 순서 상관없음
            n1 = stack.pop()
            n2 = stack.pop()
            if i == '+':
                stack.append(n1 + n2)
            else:
                stack.append(n1 * n2)
    print(f'#{t} {stack[0]}')