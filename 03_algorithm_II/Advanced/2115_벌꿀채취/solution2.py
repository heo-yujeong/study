import sys
sys.stdin = open('input.txt')

def backtrack(n, hap_honey, value, ci, cj):
    global max_value
    if hap_honey > C:
        return
    if n == M:
        max_value = max(max_value, value)
        return

    backtrack(n+1, hap_honey+honey[ci][cj+n], value+honey[ci][cj+n]**2, ci, cj)
    backtrack(n+1, hap_honey, value, ci, cj)


T = int(input())

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    memo = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            max_value = 0
            backtrack(0, 0, 0, i, j)
            memo[i][j] = max_value

    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(i1, N):
                sj = j1+M if i1 == i2 else 0
                for j2 in range(sj, N-M+1):
                    result = max(result, memo[i1][j1]+memo[i2][j2])

    print(f'#{test_case} {result}')