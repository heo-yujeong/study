# stack 클래스를 만들어서!
import sys
sys.stdin = open('input.txt')

class Stack:
    # stack을 생성할 때 크기를 지정해야 함
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, item):
        if self.is_full():
            print('Stack is full')
        else:
            self.top += 1
            self.data[self.top] = item

    def get(self):
        return self.data[self.top]

    def pop(self):
        top_value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return top_value

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.size

    # 인스턴스를 print했을 때, stack의 data를 바로 출력
    def __str__(self):
        return f'{self.data}'


T = int(input())

for test_case in range(1, T+1):
    bracket = input()
    N = len(bracket)

    stack = Stack(N)
    result = False

    for brac in bracket:
        if brac in '([{':
            stack.push(brac)
        elif brac in ')]}':
            if not stack.is_empty() and ((stack.get() == '(' and brac == ')') or (stack.get() == '[' and brac == ']') or (stack.get() == '{' and brac == '}')):
                stack.pop()
            else:
                break
    else:
        if stack.is_empty():
            result = True

    # print(stack)
    print(f'#{test_case} {result}')