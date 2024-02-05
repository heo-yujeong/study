# import sys
# sys.stdin = open('algo2_sample_in.txt')

T = int(input()) # 테스트 케이스

for test_case in range(1, T+1):
    # N: 연잎의 개수, K: 점프 횟수
    N, K = map(int, input().split())
    # 연잎의 숫자 리스트
    ai = list(map(int, input().split()))

    # 현재 위치(처음 시작은 0)
    current = 0
    # 개구리가 밟은 연잎의 숫자의 합
    result = 0
    # 직전의 값이 음수였는가?(음수였으면 1, 아니면 0)
    minus = 0
    # 점프 직전 연잎의 위치(시작은 무조건 0번이라 직전 위치도 0)
    before_idx = 0

    # K번 점프하는 동안 반복
    for i in range(K):
        # 직전 인덱스 위치의 값이 음수이면 minus는 1
        # 양수이면 minus는 0
        if ai[before_idx] < 0:
            minus = 1
        else:
            minus = 0

        # 현재 칸의 값이 0보다 크면
        if ai[current] > 0:
            # 직전 위치 값이 음수이면(한번 뒤로 갔다가 앞으로 뛰는 경우)
            if minus == 1:
                # 뒤로 간 칸만큼 더 앞으로 전진
                current = (-ai[before_idx]) + ai[current]
                # 연잎 범위를 벗어나는 경우 더 이상 점프X
                if current < 0 or current > N - 1:
                    break
                # 연잎 범위를 벗어나지 않으면 result에 현재 연잎에 적힌 번호를 더함
                result += ai[current]

            # 직전 위치 값이 양수이면
            else:
                # 현재 위치는 현재 위치에 적힌 수만큼 이동
                current += ai[current]
                # 연잎 범위를 벗어나는 경우 더 이상 점프X
                if current < 0 or current > N - 1:
                    break
                # 연잎 범위를 벗어나지 않으면 result에 현재 연잎에 적힌 번호를 더함
                result += ai[current]
            # 현재 위치가 양수임을 알려줘야 minus를 0으로 초기화 시킴
            before_idx = current

        # 현재 칸의 값이 0보다 작으면
        elif ai[current] < 0:
            # 현재 위치가 변하기 전에 직전 인덱스로 현재 위치를 입력
            before_idx = current
            # 현재 위치는 현재 위치에 적힌 수만큼 이동
            current += ai[current]
            # 연잎 범위를 벗어나는 경우 더 이상 점프X
            if current < 0 or current > N - 1:
                break
            # 연잎 범위를 벗어나지 않으면 result에 현재 연잎에 적힌 번호를 더함
            result += ai[current]

    print(f'#{test_case} {result}')