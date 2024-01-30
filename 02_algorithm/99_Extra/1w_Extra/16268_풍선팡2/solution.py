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
            hap = A[i][j]
            for p in range(4):
                pi = i + di[p]
                pj = j + dj[p]
                if 0 <= pi < N and 0 <= pj < M: # 상하좌우 이동시 범위 확인
                    hap += A[pi][pj]
            pang.append(hap)

    print(f'#{test_case} {max((pang))}')