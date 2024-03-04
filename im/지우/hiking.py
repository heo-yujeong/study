import sys
sys.stdin = open('a1.txt')

from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_k(v, k):
    if k > 1:
        directions.append((k, 0))
        directions.append((-k, 0))
    s = v
    x, y = v
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    que = deque([v])

    while que:
        v = que.pop()
        x, y = v

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    que.append((nx, ny))

                if arr[nx][ny] == 3:
                    return k

    return find_k(s, k+1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (N-1, 0)

    result = find_k(start, 1)

    print(f'#{tc} {result}')
