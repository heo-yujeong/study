import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    text = input()

    stack = []

    for txt in text:
        if stack:
            if txt == stack[-1]:
                stack.pop()
            else:
                stack.append(txt)
        else:
            stack.append((txt))

    print(f'#{test_case} {len(stack)}')