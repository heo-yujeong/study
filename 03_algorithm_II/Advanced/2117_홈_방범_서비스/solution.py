import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    city_info = [list(map(int, input().split())) for _ in range(N)]
    # 집 있음 1, 집 없음 0

    num_house = 0
    for i in range(N):
        for j in range(N):
            pass
            '''
            각 위치에서 가장 많은 집들에 제공하는 서비스 영역
            그때의 홈방법 서비스를 제공받는 집들의 수
            '''
    print(f'#{test_case} {num_house}')