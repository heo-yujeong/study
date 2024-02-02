import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) +[0] for _ in range(N)] + [[0] * (N+1)]
    # 행과 열에 0을 채운 값을 채워줌
    N += 1

    result = 0

    for i in range(N):
        cnt = 0 # i행에서 연속한 1의 개수
        for j in range(N):
            if arr[i][j]: # arr[i][j] == 1
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        for j in range(N):
            if arr[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')