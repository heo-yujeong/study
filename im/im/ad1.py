import sys
sys.stdin = open('input2.txt')
from collections import deque

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def bfs(v, k):
    if k > 1:
        dh.append(k)
        dw.append(0)
        dh.append(-k)
        dw.append(0)
    s = v
    w, h = v
    visit = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append(v)
    visit[h][w] = 1

    while queue:
        h, w = queue.popleft()

        for i in range(len(dw)):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < N and 0 <= nw < M and wall[nh][nw] and not visit[nh][nw]:
                visit[nh][nw] = 1
                queue.append((nh, nw))
                if wall[nh][nw] == 3:
                    return k

    return bfs(s, k+1)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 높이 너비
    wall = [list(map(int, input().split())) for _ in range(N)]

    start_w = N-1
    start_h = 0

    result = bfs((start_h, start_w), 1)

    print(f'#{tc} {result}')