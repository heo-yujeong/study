import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    farm_val = [list(map(int, input())) for _ in range(N)]
    profit = 0

    for i in range(N//2+1):
        for j in range(N//2-i, N//2+i+1):
            profit += farm_val[i][j] + farm_val[N-i-1][j]

    profit -= sum(farm_val[N//2])

    print(f'#{test_case} {profit}')