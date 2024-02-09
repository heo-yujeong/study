import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(start):
    visited[start] = 1
    for next in range(1, V+1):
        if not visited[next] and graph[start][next] == 1:
            dfs(next)


for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1

    S, G = map(int, input().split())

    dfs(S)

    print(f'#{test_case} {visited[G]}')