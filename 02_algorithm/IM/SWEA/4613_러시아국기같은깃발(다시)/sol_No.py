import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    cnt = 0

    for i in range(N):
        if i == 0:
            for j in range(M):
                if board[i][j] != 'W':
                    board[i][j] = 'W'
                    cnt += 1
        elif i == N-1:
            for j in range(M):
                if board[i][j] != 'R':
                    board[i][j] = 'R'
                    cnt += 1
        else:
            if i == N-2 and board[i-1][0] == 'W':
                for j in range(M):
                    if board[i][j] != 'B':
                        board[i][j] = 'B'
                        cnt += 1
            # 윗 줄이 하얀색일때
            elif board[i-1][0] == 'W':
                # 해당 행에 흰색이 더 많으면
                if board[i].count('W') >= board[i].count('B'):
                    for j in range(M):
                        if board[i][j] != 'W':
                            board[i][j] = 'W'
                            cnt += 1
                # 해당 행에 파란색이 더 많으면
                else:
                    for j in range(M):
                        if board[i][j] != 'B':
                            board[i][j] = 'B'
                            cnt += 1
            # 윗 줄이 파란색일때
            elif board[i-1][0] == 'B':
                # 해당 행에 파란색이 더 많으면
                if board[i].count('B') >= board[i].count('R'):
                    for j in range(M):
                        if board[i][j] != 'B':
                            board[i][j] = 'B'
                            cnt += 1
                # 해당 행에 빨간색이 더 많으면
                else:
                    for j in range(M):
                        if board[i][j] != 'R':
                            board[i][j] = 'R'
                            cnt += 1
            # 윗 줄이 빨간색일때
            else:
                for j in range(M):
                    if board[i][j] != 'R':
                        board[i][j] = 'R'
                        cnt += 1

    print(board)
    print(cnt)