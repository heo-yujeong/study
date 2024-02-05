import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N: N*N 글자판, M: 찾을 회문의 길이
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    result = ''
    # 가로 방향
    for i in range(N):
        for j in range(N-M+1):
            if board[i][j:j+M] == board[i][j:j+M][::-1]:
                result = board[i][j:j+M]

    # 전치행렬
    board_t = list(map(list, zip(*board)))
    for i in range(N):
        board_t[i] = ''.join(board_t[i])

    # 세로 방향
    for i in range(N):
        for j in range(N-M+1):
            if board_t[i][j:j+M] == board_t[i][j:j+M][::-1]:
                result = board_t[i][j:j+M]

    print(f'#{test_case} {result}')