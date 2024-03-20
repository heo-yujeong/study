import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start, graph):
    time = [100*N] * (N+1)
    queue = deque()
    queue.append(start)
    time[start] = 0

    while queue:
        start = queue.popleft()
        for next, w in graph[start]:
            if time[next] > time[start] + w:
                time[next] = time[start] + w
                queue.append(next)
    return time

T = int(input())

for test_case in range(1, T+1):
    N, M, X = map(int, input().split())
    go = [[] for _ in range(N+1)]
    come = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x].append([y, c])
        come[y].append([x, c])

    go_time = bfs(X, go)
    come_time = bfs(X, come)

    max_time = 0
    for i in range(1, N+1):
        max_time = max(max_time, go_time[i]+come_time[i])

    print(f'#{test_case} {max_time}')