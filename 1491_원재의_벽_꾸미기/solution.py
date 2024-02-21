import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, A, B = map(int, input().split())

    result = []
    for R in range(1, N+1):
        C = 1
        while C * R <= N:
            result.append(A * abs(R - C) + B * (N - R * C))
            C += 1

    print(f'#{test_case} {min(result)}')