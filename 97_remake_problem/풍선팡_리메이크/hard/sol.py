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

    max_pang = []

    for i in range(N):
        for j in range(M):
            pang = set()
            pang_num = 0
            result = 0
            pang.add((i, j))
            # 1번 시도 = 짝수
            if board[i][j] % 2 == 0:
                for k in range(4):
                    nx = i + dx1[k]
                    ny = j + dy1[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang.add((nx, ny))
                for x, y in pang:
                    pang_num += board[x][y]
                # 1번 시도 결과 = 짝수
                if pang_num % 2 == 0:
                    for a in range(N):
                        for b in range(M):
                            pang.add((a, b))
                            if board[a][b] % 2 == 0:
                                for c in range(4):
                                    na = a + dx1[c]
                                    nb = b + dy1[c]
                                    if 0 <= na < N and 0 <= nb < M:
                                        pang.add((na, nb))
                            else:
                                for c in range(4):
                                    na = a + dx2[c]
                                    nb = b + dy2[c]
                                    if 0 <= na < N and 0 <= nb < M:
                                        pang.add((na, nb))
            # 첫번째 시도 = 홀수
            else:
                for k in range(4):
                    nx = i + dx2[k]
                    ny = j + dy2[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        pang.add((nx, ny))
                for x, y in pang:
                    pang_num += board[x][y]
                # 1번 시도 결과 = 홀수
                if pang_num % 2 != 0:
                    for a in range(N):
                        for b in range(M):
                            pang.add((a, b))
                            if board[a][b] % 2 == 0:
                                for c in range(4):
                                    na = a + dx1[c]
                                    nb = b + dy1[c]
                                    if 0 <= na < N and 0 <= nb < M:
                                        pang.add((na, nb))
                            else:
                                for c in range(4):
                                    na = a + dx2[c]
                                    nb = b + dy2[c]
                                    if 0 <= na < N and 0 <= nb < M:
                                        pang.add((na, nb))

            for x, y in pang:
                result += board[x][y]
            max_pang.append(result)
            print(pang, result)
    print(f'#{tc} {max(max_pang)}')