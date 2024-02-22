import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_die = []

    for i in range(N):
        for j in range(N):
            die = 0
            for k in range(i-M//2, i+M//2+1):
                for l in range(j-M//2, j+M//2+1):
                    if 0 <= k < N and 0 <= l < N and abs(k-i) + abs(l-j) <= M//2:
                        die += board[k][l]
            max_die.append(die)

    print(f'#{tc} {max(max_die)}')