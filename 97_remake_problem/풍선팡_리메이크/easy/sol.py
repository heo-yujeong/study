import sys
sys.stdin = open('input.txt')

dx1 = [0, 0, -1, 1]
dy1 = [-1, 1, 0, 0]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_pang = []

    for i in range(N):
        for j in range(M):
            pang = board[i][j]
            if pang % 2 == 0:
                for k in range(4):
                    nx = i + dx1[k]
                    ny = j + dy1[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang += board[nx][ny]
            else:
                for k in range(4):
                    nx = i + dx2[k]
                    ny = j + dy2[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang += board[nx][ny]
            max_pang.append(pang)

    print(f'#{tc} {max(max_pang)}')