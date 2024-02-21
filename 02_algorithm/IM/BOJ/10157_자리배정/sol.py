import sys
sys.stdin = open('input.txt')

# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

C, R = map(int, input().split())
K = int(input())
seat = [[0] * R for _ in range(C)]

num = 1
x = y = 0
seat[x][y] = num
num += 1
idx = 0

if R * C < K:
    print(0)
else:
    while num <= K:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < C and 0 <= ny < R and seat[nx][ny] == 0:
            seat[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            idx += 1
            if idx == 4:
                idx = 0

    for i in range(C):
        for j in range(R):
            if seat[i][j] == K:
                print(i+1, j+1)