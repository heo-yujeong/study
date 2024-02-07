import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    stack = []
    stack.append(start)

    while stack:
        now = stack.pop()
        visited[now] = 1
        for next in range(1, 100):
            if not visited[next] and graph[now][next] == 1:
                if next == end:
                    return 1
                stack.append(next)
    return 0

for _ in range(10):
    T, N = map(int, input().split())

    connect = list(map(int, input().split()))
    graph = [[0] * 101 for _ in range(101)]
    visited = [0] * 101
    for n in range(N):
        start, end = connect.pop(0), connect.pop(0)
        graph[start][end] = 1

    result = dfs(0, 99)

    print(f'#{T} {result}')