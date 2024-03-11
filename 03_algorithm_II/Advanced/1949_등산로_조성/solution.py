import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x, iscut):
    global max_len

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[ny][nx]:
            if map_info[y][x] > map_info[ny][nx]:
                    visit[ny][nx] = visit[y][x] + 1
                    dfs(ny, nx, iscut)
                    if max_len < visit[ny][nx]:
                        max_len = visit[ny][nx]
                    visit[ny][nx] = 0
            if map_info[y][x] <= map_info[ny][nx]:
                if not iscut:
                    for l in range(map_info[ny][nx]-map_info[y][x]+1, K+1):
                        if map_info[ny][nx] - l < map_info[y][x]:
                            map_info[ny][nx] -= l
                            iscut = True
                            visit[ny][nx] = visit[y][x] + 1
                            dfs(ny, nx, iscut)
                            if max_len < visit[ny][nx]:
                                max_len = visit[ny][nx]
                            map_info[ny][nx] += l
                            iscut = False
                            visit[ny][nx] = 0

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height < map_info[i][j]:
                max_height = map_info[i][j]
    start_lst = []
    for i in range(N):
        for j in range(N):
            if max_height == map_info[i][j]:
                start_lst.append((i, j))

    max_len = 0

    for start_y, start_x in start_lst:
        visit[start_y][start_x] = 1
        dfs(start_y, start_x, False)
        visit[start_y][start_x] = 0

    print(f'#{test_case} {max_len}')