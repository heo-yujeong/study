import sys
sys.stdin = open('input.txt')

def dfs(start):
    visited[start] = 1
    for next in range(100):
        if not visited[next] and graph[start][next] == 1:
            dfs(next)


for _ in range(10):
    T, N = map(int, input().split())

    connect = list(map(int, input().split()))
    graph = [[0] * 101 for _ in range(101)]
    visited = [0] * 101
    for n in range(N):
        start, end = connect.pop(0), connect.pop(0)
        graph[start][end] = 1

    dfs(0)

    print(f'#{T} {visited[99]}')