import sys
sys.stdin = open('input.txt')

def select_plan(month, fee):
    global min_fee

    if month >= 13:
        if min_fee > fee:
            min_fee = fee
    else:
        select_plan(month + 1, fee + d_fee * plans[month])
        select_plan(month + 1, fee + m_fee)
        select_plan(month + 3, fee + m3_fee)

T = int(input())

for test_case in range(1, T + 1):
    d_fee, m_fee, m3_fee, y_fee = map(int, input().split())
    plans = [0] + list(map(int, input().split()))

    min_fee = y_fee

    select_plan(0, 0)

    print(f'#{test_case} {min_fee}')