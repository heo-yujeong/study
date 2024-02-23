import sys
sys.stdin = open('input.txt')

dx1 = [0, 0, -1, 1]
dy1 = [-1, 1, 0, 0]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_pang = 0

    for i in range(N):
        for j in range(M):
            result = 0
            pang = set()
            pang_num = board[i][j]
            pang_num2 = 0
            pang.add((i, j))

            if board[i][j] % 2 == 0:
                for k in range(4):
                    nx = i + dx1[k]
                    ny = j + dy1[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang_num += board[nx][ny]
                        pang.add((nx, ny))

                    if board[i][j] % 2 == pang_num % 2:
                        for a in range(N):
                            for b in range(M):
                                pang_num2 = board[a][b]
                                if (a, b) not in pang:
                                    if board[a][b] % 2 == 0:
                                        for c in range(4):
                                            mx = a + dx1[c]
                                            my = b + dy1[c]
                                            if 0 <= mx < N and 0 <= my < M and (mx, my) not in pang:
                                                pang_num2 += board[mx][my]
                                        result = pang_num + pang_num2
                                        if max_pang < result:
                                            max_pang = result
                                    else:
                                        for c in range(4):
                                            mx = a + dx2[c]
                                            my = b + dy2[c]
                                            if 0 <= mx < N and 0 <= my < M and (mx, my) not in pang:
                                                pang_num2 += board[mx][my]
                                        result = pang_num + pang_num2
                                        if max_pang < result:
                                            max_pang = result
            else:
                for k in range(4):
                    nx = i + dx2[k]
                    ny = j + dy2[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang_num += board[nx][ny]
                        pang.add((nx, ny))
                    if board[i][j] % 2 == pang_num % 2:
                        for a in range(N):
                            for b in range(M):
                                pang_num2 = board[a][b]
                                if (a, b) not in pang:
                                    if board[a][b] % 2 == 0:
                                        for c in range(4):
                                            mx = a + dx1[c]
                                            my = b + dy1[c]
                                            if 0 <= mx < N and 0 <= my < M and (mx, my) not in pang:
                                                pang_num2 += board[mx][my]
                                        result = pang_num + pang_num2
                                        if max_pang < result:
                                            max_pang = result
                                    else:
                                        for c in range(4):
                                            mx = a + dx2[c]
                                            my = b + dy2[c]
                                            if 0 <= mx < N and 0 <= my < M and (mx, my) not in pang:
                                                pang_num2 += board[mx][my]
                                        result = pang_num + pang_num2
                                        if max_pang < result:
                                            max_pang = result

    print(f'#{tc} {max_pang}')