import sys
sys.stdin = open('input.txt')

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

def dfs(y, x, idx, dessert_lst):
    global max_dessert

    for i in range(idx, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] in [0, 2]:
            if cafe[ny][nx] in dessert_lst:
                if visit[ny][nx] == 2 and len(dessert_lst) > 2:
                    max_dessert = max(max_dessert, len(dessert_lst))
                    return
                continue

            visit[ny][nx] = 1
            dfs(ny, nx, i, dessert_lst+[cafe[ny][nx]])
            visit[ny][nx] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    max_dessert = -1

    for i in range(N):
        for j in range(N):
            visit[i][j] = 2
            dfs(i, j, 0, [cafe[i][j]])
            visit[i][j] = 0

    print(f'#{test_case} {max_dessert}')