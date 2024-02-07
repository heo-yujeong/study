import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):
    text = input()

    # 들어온 문자를 하나씩 stack에 저장하면서
    # (stack이 비어 있지 않은 동안)
    # stack의 가장 위에 있는 문자와 들어온 문자가 같으면
    # pop해서 빼고, 같지 않으면 push
    stack = []

    for txt in text:
        if stack:
            if txt == stack[-1]:
                stack.pop()
            else:
                stack.append(txt)
        else:
            stack.append(txt)

    print(f'#{test_case} {len(stack)}')