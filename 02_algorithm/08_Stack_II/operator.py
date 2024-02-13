'''
(6 + 5 * ( 2 - 8 ) / 2)
'''

top = -1
stack = [0] * 100

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선순위

infix = '(6+5*(2-8)/2)'
postfix = ''

for tk in infix:
    # 여는 괄호는 push
    # 연산자이고 top 원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        top += 1
        stack[top] = tk
    # 연산자이고 top 원소보다 우선순위가 높지 않으면
    # top 원소의 우선순위가 낮을 때까지 pop
    # 그 후 push
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
        while isp[stack[top]] >= icp[tk]:
            top -= 1
            postfix += stack[top + 1]
            stack[top + 1] = 0
        top += 1
        stack[top] = tk
    # 닫는 괄호면, 여는 괄호를 만날 때까지 pop
    elif tk == ')':
        while stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
            stack[top + 1] = 0
        # 여는 괄호 pop해서 버림
        top -= 1
        stack[top + 1] = 0
    # 피연산자이면 바로 출력
    else:
        postfix += tk

print(postfix)