import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    city_info = [list(map(int, input().split())) for _ in range(N)]
    # 집 있음 1, 집 없음 0
    house = []
    for i in range(N):
        for j in range(N):
            if city_info[i][j]:
                house.append((i, j))

    max_num_house = 0

    for K in range(1, N+2):
        cost = K ** 2 + (K-1) ** 2
        for i in range(N):
            for j in range(N):
                num_house = 0
                for x, y in house:
                    if abs(x-i) + abs(y-j) <= K-1:
                        num_house += 1
                if M * num_house >= cost:
                    max_num_house = max(max_num_house, num_house)

    print(f'#{test_case} {max_num_house}')