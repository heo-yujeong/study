import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    loc = 0 # 현재 위치
    count = 0 # 충전 횟수

    while loc + K < N:
    # 현재 위치 + 최대 이동거리가 종점에 도착하지 않을 동안 반복
        for step in range(K, 0, -1):
        # 최대한 멀리있는 정류장에서 충전하는 것이 최소 충전 횟수
            if loc + step in stations:
                loc += step
                count += 1
                break
        else:
        # 종점에 도착할 수 없는 경우 = step이 0이 되었는데 충전소가 나타나지 않은 경우
            count = 0
            break

    print(f'#{test_case} {count}')

# 방법2
'''
T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # gas : 이동 가능 횟수, now : 현재 정류장 위치, cnt : 충전 횟수
    def go(gas, now, cnt):
        global result
        # result에 더 큰 값이 온다면 더이상 조사X
        if cnt > result:
            return
        # 종착점 도착 시 멈춤
        if now == N:
            result = cnt
            return
        if station[now]:
            go(K-1, now+1, cnt+1) # 충전 후 다음 칸으로 갈때 가스 -1
        # 현재 위치에 충전소가 없으면 한칸 이동!(가스가 남아 있는 동안)
        if gas:
            go(gas-1, now+1, cnt)

    # 실제 정류장이 있는 곳 => station에
    station = [0] * (N+1)
    for idx in range(M):
        station[data[idx]] = True
    result = N + 1 # 최악의 개수로 선언(모든 충전소를 다 들린다!)

    go(K, 0, 0)
    if result == N + 1:
        result = 0

    print(f'#{test_case} {result}')
'''