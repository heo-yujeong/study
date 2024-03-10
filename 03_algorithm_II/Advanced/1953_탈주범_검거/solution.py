import sys
sys.stdin = open('input.txt')
from collections import deque

able_dir = {1: [[-1, 0], [1, 0], [0, -1], [0, 1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [0, 1]],
            4: [[-1, 0], [0, 1]],
            5: [[1, 0], [0, 1]],
            6: [[1, 0], [0, -1]],
            7: [[-1, 0], [0, -1]]}

def bfs(h, w, dir):
    queue = deque()
    queue.append((h, w, dir))
    visit[R][C] = 1

    while queue:
        h, w, dir = queue.popleft()
        for dh, dw in able_dir[dir]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < N and 0 <= nw < M and tunnel[nh][nw] and not visit[nh][nw]:
                if visit[h][w] == L:
                    return
                for dh2, dw2 in able_dir[tunnel[nh][nw]]:
                    nh2 = nh + dh2
                    nw2 = nw + dw2
                    if (nh2, nw2) == (h, w):
                        queue.append((nh, nw, tunnel[nh][nw]))
                        visit[nh][nw] = visit[h][w] + 1

T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]

    num_place = 0

    bfs(R, C, tunnel[R][C])
    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                num_place += 1

    print(f'#{test_case} {num_place}')