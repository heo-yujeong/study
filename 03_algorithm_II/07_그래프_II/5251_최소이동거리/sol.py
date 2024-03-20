import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 0

    while queue:
        start = queue.popleft()
        for next, w in graph[start]:
            if visit[next] > visit[start] + w:
                visit[next] = visit[start] + w
                queue.append(next)

T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visit = [10*N] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    bfs(0)

    print(f'#{test_case} {visit[N]}')