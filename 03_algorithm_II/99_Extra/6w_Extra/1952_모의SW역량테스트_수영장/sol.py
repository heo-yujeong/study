import sys
sys.stdin = open('input.txt')

# 월 체크, 요금
def select_plan(month, fee):
    global min_fee

    # 모든 달을 다 고려했다면
    if month >= 13:
        # 최소 비용으로 업데이트
        if min_fee > fee:
            min_fee = fee
        return
    # 1일 권을 구매한 경우
    select_plan(month + 1, fee + d_fee * plans[month])
    # 1달 권을 구매한 경우
    select_plan(month + 1, fee + m_fee)
    # 3달 권을 구매한 경우
    select_plan(month + 3, fee + m3_fee)

# 테스트 케이스
T = int(input())

for test_case in range(1, T + 1):
    # 1일, 1달, 3달, 1년 요금
    d_fee, m_fee, m3_fee, y_fee = map(int, input().split())
    # 이용 계획(달을 인덱스로 이용하기 위해 0 추가)
    plans = [0] + list(map(int, input().split()))

    # 연간 이용권을 최소값으로 초기화
    min_fee = y_fee

    select_plan(0, 0)

    print(f'#{test_case} {min_fee}')