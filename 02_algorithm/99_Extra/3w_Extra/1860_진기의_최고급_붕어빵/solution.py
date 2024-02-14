import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N: 사람 수, M: 붕어빵 만드는데 걸리는 시간, K: 붕어빵 개수
    N, M, K = map(int, input().split())
    # 손님 도착 시간
    arr_time = list(map(int, input().split()))
    arr_time.sort()
    result = 'Possible'

    for i in range(N):
        # 손님이 도착했을 때 만든 붕어빵의 수
        # = 손님 도착 시간 / 붕어빵 만드는데 걸리는 시간 * 갯수
        # 그 수가 손님 수보다 작으면 제공 불가!
        # 손님 도착시간을 작은 순으로 정렬했기 때문
        if arr_time[i]//M*K < i+1:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')