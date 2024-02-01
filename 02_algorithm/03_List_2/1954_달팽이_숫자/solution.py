import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N * N 크기의 달팽이
    N = int(input())
    # 결과를 출력할 2차원 배열
    result = [[0] * N for _ in range(N)]
    # 이미 값이 들어있는지 확인할 2차원 배열(result와 같은 크기)
    visited = [[0] * N for _ in range(N)]
    # 1부터 달팽이를 채울 값 - ex) N = 2 => 1 ~ 4까지
    num_list = [i+1 for i in range(N**2)]
    # num_list의 인덱스 ( 0 ~ N**2-1)
    idx = 0

    # 이동할 방향
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0] #  0  1  2  3
    d_idx = 0 # 방향 바꿔줄 인덱스

    # result의 값을 채우면 자동으로 2가지 일 수행
    # 1. idx 값 1 증가 => 동일한 값을 result에 넣지 않기 위해
    # 2. visited에 1 넣기기
    result[0][0] = num_list[idx]
    idx += 1
    visited[0][0] = 1

    # 행열 인덱스 초기화
    i = j = 0
    while True: # 종료조건이 있을 때까지 반복
        mx = i + dx[d_idx]
        my = j + dy[d_idx]
        # mx, my가 유효한 인덱스라면
        # 1. 달팽이(2차원 배열)를 벗어나지 않음
        # 2. visited가 0임
        if 0 <= mx < N and 0 <= my < N and visited[mx][my] == 0:
            # i, j의 값을 바꿔주고 result에 값 넣음
            i = mx
            j = my
            result[i][j] = num_list[idx]
            visited[i][j] = 1
            idx += 1
        else:
            # 유효한 인덱스가 아니면
            # 방향을 바꿤 (우(0) -> 하(1) -> 왼(2) -> 위(3))
            d_idx += 1
            if d_idx == 4:
                d_idx = 0

        # 종료조건 : num_list의 리스트를 벗어날 때 = idx = n ** 2
        if idx == N**2:
            break

    print(f'#{test_case}')
    for res in result:
        print(*res)