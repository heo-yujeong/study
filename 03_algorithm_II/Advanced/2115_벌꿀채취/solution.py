import sys
sys.stdin = open('input.txt')

def dfs(n, hap_honey, value, ci, cj):
    global max_value
    if hap_honey > C:
        return
    if n == M:
        max_value = max(max_value, value)
        return

    dfs(n+1, hap_honey+honey[ci][cj+n], value+honey[ci][cj+n]**2, ci, cj)
    dfs(n+1, hap_honey, value, ci, cj)


T = int(input())

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i1 in range(N):
        for j1 in range(N-M+1):
            max_value = 0
            dfs(0, 0, 0, i1, j1)
            max_fir = max_value
            for i2 in range(i1, N):
                sj = j1+M if i1 == i2 else 0
                for j2 in range(sj, N-M+1):
                    max_value = 0
                    dfs(0, 0, 0, i2, j2)
                    result = max(result, max_fir+max_value)

    print(f'#{test_case} {result}')