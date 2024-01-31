import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    ai.sort()
    result = []

    for i in range(len(ai)):
        if i % 2 == 0:
            result.append(ai.pop())
        else:
            result.append(ai.pop(0))

    print(f'#{test_case}', *result)