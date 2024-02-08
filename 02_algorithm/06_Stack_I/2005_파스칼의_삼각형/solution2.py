# DP

import sys
sys.stdin = open('input.txt')

memo = [[1] * 10 for _ in range(10)]
for i in range(1, 10):
    for j in range(1, i+1):
        if i != j:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(N):
        print(*memo[i][:i+1])