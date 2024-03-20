import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    dist[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                diff = max(height[ny][nx] - height[y][x], 0)
                if dist[ny][nx] > dist[y][x] + diff + 1:
                    dist[ny][nx] = dist[y][x] + diff + 1
                    queue.append((ny, nx))

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]

    dist = [[2001] * N for _ in range(N)]

    bfs(0, 0)

    print(f'#{test_case} {dist[N-1][N-1]}')