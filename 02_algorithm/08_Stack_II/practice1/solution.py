# 수식문자열을 읽어 피연산자는 바로 출력하고
# 연산자는 스택에 push하여 수식이 끝나면 스택의 남아있는 연산자를
# 모두 pop하여 출력하시오. 연산자는 사칙 연산만 사용하시오.

# 출력 결과 : 2 3 4 5 / * +

import sys
sys.stdin = open('input.txt')

math_exp = input().split()

stack = []
oper = '+-*/'

for token in math_exp:
    if token in oper:
        stack.append(token)
    else:
        print(token, end=' ')

else:
    for _ in range(len(stack)):
        print(stack.pop(), end=' ')