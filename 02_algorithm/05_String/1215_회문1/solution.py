import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input()) # 회문 길이
    board = [input() for _ in range(8)]

    result = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8-N+1):
            if board[i][j:j+N] == board[i][j:j+N][::-1]:
                result += 1

    board_t = [''.join(list(i)) for i in zip(*board)]

    # 세로 탐색
    for i in range(8):
        for j in range(8-N+1):
            if board_t[i][j:j+N] == board_t[i][j:j+N][::-1]:
                result += 1

    print(f'#{test_case} {result}')