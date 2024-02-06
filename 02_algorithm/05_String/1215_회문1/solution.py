import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input()) # 회문 길이
    board = [input() for _ in range(8)]

    result = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8-N+1):
            # N 길이의 값과 그 값을 뒤집은 값이 같다면
            if board[i][j:j+N] == board[i][j:j+N][::-1]:
                # 결과 + 1 => 회문 갯수 증가
                result += 1

    # 전치행렬
    board_t = [''.join(list(i)) for i in zip(*board)]

    # 세로 탐색
    for i in range(8):
        for j in range(8-N+1):
            if board_t[i][j:j+N] == board_t[i][j:j+N][::-1]:
                result += 1

    print(f'#{test_case} {result}')