import sys
sys.stdin = open('input.txt')

infix = input().split()
postfix = []
stack = []

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선순위

for token in infix:
    if token == '(' or (token in '+-*/' and isp[stack[-1]] < icp[token]):
        stack.append(token)
    elif token in '+-*/' and isp[stack[-1]] >= icp[token]:
        while isp[stack[-1]] >= icp[token]:
            postfix.append(stack.pop())
        stack.append(token)
    elif token == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        postfix.append(token)

print(*postfix)