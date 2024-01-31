import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0] # 상하좌우
    dj = [0, 0, -1, 1]

    pang = []

    for i in range(N):
        for j in range(M):
            num = A[i][j]
            hap = A[i][j]
            for k in range(4):
                for l in range(1, num+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        hap += A[ni][nj]
            pang.append(hap)

    print(f'#{test_case} {max(pang)}')