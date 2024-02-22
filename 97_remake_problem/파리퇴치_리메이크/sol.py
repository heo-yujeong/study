import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    die_list = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            die = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    die += board[k][l]
            for k in range(i+1, i+M-1):
                for l in range(j+1, j+M-1):
                    die -= board[k][l]
            die_list.append(die)

    print(f'#{tc} {max(die_list)}')