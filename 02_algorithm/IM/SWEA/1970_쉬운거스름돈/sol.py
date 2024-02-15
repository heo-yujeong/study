import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    total_money = int(input())
    money_count = [0] * 8
    money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for unit in money_unit:
        if total_money >= unit:
            money_count[money_unit.index(unit)] = total_money // unit
            total_money = total_money % unit

    print(f'#{test_case}')
    print(*money_count)