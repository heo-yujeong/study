import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    min_cnt = N*M

    for first_bar in range(1, N-1):
        for second_bar in range(first_bar+1, N):
            cnt = 0
            for i in range(first_bar):
                for j in range(M):
                    if board[i][j] != 'W':
                        cnt += 1
            for i in range(first_bar, second_bar):
                for j in range(M):
                    if board[i][j] != 'B':
                        cnt += 1
            for i in range(second_bar, N):
                for j in range(M):
                    if board[i][j] != 'R':
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{test_case} {min_cnt}')