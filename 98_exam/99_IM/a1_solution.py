import sys
sys.stdin = open('a1_input.txt')
from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(v, k):
    if k > 1:
        directions.append((k, 0))
        directions.append((-k, 0))
    s = v
    h, w = v
    visit = [[0] * M for _ in range(N)]
    queue = deque([v])
    visit[h][w] = 1

    while queue:
        v = queue.popleft()
        h, w = v

        for dh, dw in directions:
            nh, nw = h + dh, w + dw
            if 0 <= nh < N and 0 <= nw < M:
                if wall[nh][nw] == 1 and not visit[nh][nw]:
                    visit[nh][nw] = 1
                    queue.append([nh, nw])

                if wall[nh][nw] == 3:
                    return k

    return bfs(s, k+1)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 높이 너비
    wall = [list(map(int, input().split())) for _ in range(N)]

    start = (N-1, 0)

    result = bfs(start, 1)

    print(f'#{tc} {result}')