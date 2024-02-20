import sys
sys.stdin = open('input.txt')

def check():
    # 가로로 5개
    for i in range(N):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if board[i][j+k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'

    # 세로로 5개
    for i in range(N):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if board[j+k][i] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'

    # 좌상우하 5개
    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if board[i+k][j+k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'

    # 우상좌하 5개
    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if board[i+k][j+4-k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'
    return 'NO'

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    print(f'#{test_case} {check()}')