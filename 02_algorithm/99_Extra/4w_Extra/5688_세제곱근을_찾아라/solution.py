import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = -1

    for i in range(1, N+1):
        if i ** 3 > N:
            break
        if i ** 3 == N:
            result = i
            break

    print(f'#{test_case} {result}')