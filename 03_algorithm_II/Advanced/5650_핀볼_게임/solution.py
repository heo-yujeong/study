import sys
sys.stdin = open('input.txt')

# 상0 하1 좌2 우3
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

dir_trans = {1:[1, 3, 0, 2],
             2:[3, 0, 1, 2],
             3:[2, 0, 3, 1],
             4:[1, 2, 3, 0],
             5:[1, 0, 3, 2]}

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    holes = {} # (i, j) = 행, 열
    for i in range(N):
        for j in range(N):
            if board[i][j] in range(6, 11):
                if holes.get(board[i][j], None) == None:
                    holes[board[i][j]] = [(i, j)]
                else:
                    holes[board[i][j]].append((i, j))

    max_jumsu = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for dir in range(4):
                    ni, nj = i, j
                    jumsu = 0
                    while True:
                        ni += di[dir]
                        nj += dj[dir]
                        if ni < 0 or nj < 0 or ni > N-1 or nj > N-1:
                            jumsu += 1
                            dir = dir_trans[5][dir]
                        elif (ni, nj) == (i, j) or board[ni][nj] == -1:
                            max_jumsu = max(max_jumsu, jumsu)
                            break
                        elif board[ni][nj] in range(1, 6):
                            jumsu += 1
                            dir = dir_trans[board[ni][nj]][dir]
                        elif board[ni][nj] in range(6, 11):
                            lst = holes[board[ni][nj]]
                            if lst[0] == (ni, nj):
                                ni, nj = lst[1]
                            else:
                                ni, nj = lst[0]

    print(f'#{test_case} {max_jumsu}')