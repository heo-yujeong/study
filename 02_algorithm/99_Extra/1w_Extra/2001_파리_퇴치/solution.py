import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [] # 죽은 파리의 수

    for i in range(N-M+1):
        for j in range(N-M+1):
            hap = 0 # M * M 안에 있는 파리의 수
            for k in range(i, i+M):
                for l in range(j, j+M):
                    hap += arr[k][l]
            result.append(hap)

    print(f'#{test_case} {max(result)}')
