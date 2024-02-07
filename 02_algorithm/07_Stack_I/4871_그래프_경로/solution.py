import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(start, end):
    stack = []
    stack.append(start)

    while stack:
        now = stack.pop()
        visited[now] = 1
        for next in range(1, V+1):
            if not visited[next] and graph[now][next] == 1:
                if next == end:
                    return 1
                stack.append(next)
    return 0

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1

    S, G = map(int, input().split())

    result = dfs(S, G)

    print(f'#{test_case} {result}')