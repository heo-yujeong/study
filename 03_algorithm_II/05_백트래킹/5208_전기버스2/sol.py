import sys
sys.stdin = open('input.txt')

# 현재 위치, 교환 횟수
def backtrack(loc, cnt):
    global min_charge
    # 현재 위치 == 도착지점이라면
    if loc == N-1:
        # 작은 값으로 저장
        min_charge = min(cnt, min_charge)
        return

    # 도착하지 않았는데 이미 최소 충전횟수 넘어섰다면 가지치기
    if cnt >= min_charge:
        return

    # 현재 위치에서 갈 수 있는 곳을 모두 탐색
    # 1 ~ 현재 위치의 배터리 용량
    for i in range(1, M[loc]+1):
        backtrack(loc+i, cnt+1)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 정류장 수, M: 정류장 별 배터리 용량
    N, *M = map(int, input().split())

    # 최소 교환횟수 초기화 = 모든 정류장에서 교환했을 때가 최악
    min_charge = N
    # 현재 위치 0, 교환횟수 -1
    # => 출발지 에서의 배터리 장착은 횟수에서 제외하기 때문
    backtrack(0, -1)

    print(f'#{test_case} {min_charge}')