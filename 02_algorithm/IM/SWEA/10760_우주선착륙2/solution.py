import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if area[i][j] > area[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                result += 1

    print(f'#{test_case} {result}')