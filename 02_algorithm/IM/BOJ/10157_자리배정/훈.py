x, y = map(int, input().split())
num = int(input())

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visit = [[0]*y for _ in range(x)]
cnt = 0
nx = 0
ny = 0

if num > x * y:
    print(0)
else:
    for i in range(1, x*y+1):
        if i == num:
            print(nx+1, ny+1)
        else:
            visit[nx][ny] = 1
            nx += dx[cnt]
            ny += dy[cnt]
            if nx < 0 or nx >= x or ny < 0 or ny >= y or visit[nx][ny]:
                nx -= dx[cnt]
                ny -= dy[cnt]
                cnt = (cnt + 1) % 4
                nx += dx[cnt]
                ny += dy[cnt]