import sys
sys.stdin = open('input.txt')

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M, B = map(int, input().split()) # 판크기, 파리채크기, 방사능파리
    bangsa = [list(map(int, input().split())) for _ in range(B)]
    board = [list(map(int, input().split())) for _ in range(N)]

    max_die = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            die = set()
            die_num = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    die.add((k, l))
                    if [k+1, l+1] in bangsa:
                        for idx in range(4):
                            nx = k + dx[idx]
                            ny = l + dy[idx]
                            if 0 <= nx < N and 0 <= ny < N:
                                die.add((nx, ny))
            for x, y in die:
                die_num += board[x][y]
            max_die.append(die_num)

    print(f'#{tc} {max(max_die)}')