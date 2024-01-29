import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    mat_90 = [[0 for _ in range(N)] for _ in range(N)]
    mat_180 = [[0 for _ in range(N)] for _ in range(N)]
    mat_270 = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            mat_90[i][j] = mat[N-j-1][i]
    for i in range(N):
        for j in range(N):
            mat_180[i][j] = mat_90[N-j-1][i]
    for i in range(N):
        for j in range(N):
            mat_270[i][j] = mat_180[N-j-1][i]

    print(f'#{test_case}')
    for i in range(N):
        for a in range(N):
            print(mat_90[i][a], end='')
        print(end=' ')
        for b in range(N):
            print(mat_180[i][b], end='')
        print(end=' ')
        for c in range(N):
            print(mat_270[i][c], end='')
        print()