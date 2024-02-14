import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N: 사람 수, M: 붕어빵 만드는데 걸리는 시간, K: 붕어빵 개수
    N, M, K = map(int, input().split())
    # 손님 도착 시간
    arr_time = list(map(int, input().split()))
    arr_time.sort()
    # 붕어빵을 제공할 수 없다고 가정
    result = 'Impossible'

    # 각 초마다 만들 수 있는 붕어빵의 수
    # sum(bread_count[0:초+1]) = 해당 초에 만들어지는 붕어빵 수
    bread_count = [0] * (max(arr_time) + 1)
    for i in range(len(bread_count)):
        if i > 0 and i % M == 0:
            bread_count[i] = K

    # 모든 손님 순회
    for time in arr_time:
        # 손님이 왔을 시간에 1개 이상의 붕어빵이 있으면
        if sum(bread_count[:time+1]) >= 1:
            # 붕어빵 1개를 감소
            for i in range(time):
                if bread_count[i] >= 1:
                    bread_count[i] -= 1
                    break
        # 붕어빵이 없으면 더이상 손님 순회하지 않고 종료
        else:
            break
    # 모든 손님을 순회한 후에
    else:
        # 붕어빵 수가 모두 0 이상이면
        if min(bread_count) >= 0:
            # 제공할 수 있다!
            result = 'Possible'

    print(f'#{test_case} {result}')