import sys
sys.stdin = open('input.txt')

def BFS(start, end):
    queue = []
    queue.append(start)
    visited[start] = 1

    while queue:
        start = queue.pop(0)
        for next in range(1, V+1):
            if graph[start][next] == 1 and visited[next] == 0:
                visited[next] = visited[start] + 1
                queue.append(next)
                if next == end:
                    return

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 1

    S, G = map(int, input().split())

    BFS(S, G)

    print(f'#{test_case} {visited[G]-1 if visited[G] else 0}')