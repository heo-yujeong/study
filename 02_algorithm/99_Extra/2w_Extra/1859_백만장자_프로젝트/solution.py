import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    profit = 0

    for i in range(N-2, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += (max_price - price[i])

    print(f'#{test_case} {profit}')