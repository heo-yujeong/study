import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def check(x, y):
    for i in range(8):
        change = []
        for j in range(1, N):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    break
                elif board[nx][ny] == color:
                    for _ in range(len(change)):
                        cx, cy = change.pop()
                        board[cx][cy] = color
                    break
                else:
                    change.append((nx, ny))

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1 # 1 = 흑돌
    board[N//2][N//2] = board[N//2-1][N//2-1] = 2 # 2 = 백돌

    for _ in range(M):
        y, x, color = map(int, input().split())
        x, y = x-1, y-1
        board[x][y] = color
        check(x, y)

    count_w = count_b = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count_b += 1
            elif board[i][j] == 2:
                count_w += 1

    print(f'#{test_case} {count_b} {count_w}')