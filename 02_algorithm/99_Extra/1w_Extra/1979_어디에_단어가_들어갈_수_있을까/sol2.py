import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        r = 0
        c = 0
        for j in range(N):
            if arr[i][j]:
                c += 1
            else:
                if c == K:
                    cnt += 1
                c = 0
            if arr[j][i]:
                r += 1
            else:
                if r == K:
                    cnt += 1
                r = 0
        # 가장자리가 1인 경우 = 마지막이 1인 경우
        if c == K:
            cnt += 1
            c = 0
        if r == K:
            cnt += 1
            r = 0

    print(f'#{tc} {cnt}')