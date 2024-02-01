# 1. 오름차순 정렬
# 2. 새로운 N*N배열 만들어서
# 3. 나선형 배열로 정렬하기

import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
num_list_one = []
# num_list의 차원 줄이기 => 2차원 -> 1차원
for num in num_list:
    for n in num:
        num_list_one.append(n)

# 선택정렬(오름차순으로)
for i in range(len(num_list_one)-1):
        min_idx = i
        for j in range(i+1, len(num_list_one)):
            if num_list_one[min_idx] > num_list_one[j]:
                min_idx = j
        num_list_one[min_idx], num_list_one[i] = num_list_one[i], num_list_one[min_idx]

# num_list_one의 인덱스 ( 0 ~ N )
idx = 0
result = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 이동할 방향
dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0] #  0  1  2  3
d_idx = 0 # 방향 바꿔줄 인덱스

# result의 값을 채우면 자동으로 2가지 일 수행
# 1. idx 값 1 증가 => 동일한 값을 result에 넣지 않기 위해
# 2. visited에 1 넣기기
result[0][0] = num_list_one[idx]
idx += 1
visited[0][0] = 1

# 행열 인덱스 초기화
i = j = 0
while True: # 종료조건이 있을 때까지 반복
    mx = i + dx[d_idx]
    my = j + dy[d_idx]
    # mx, my가 유효한 인덱스라면
    # 1. 2차원 배열을 벗어나지 않음
    # 2. visited가 0임
    if 0 <= mx < N and 0 <= my < N and visited[mx][my] == 0:
        # i, j의 값을 바꿔주고 result에 값 넣음
        i = mx
        j = my
        result[i][j] = num_list_one[idx]
        visited[i][j] = 1
        idx += 1
    else:
        # 유효한 인덱스가 아니면
        # 방향을 바꿤 (우(0) -> 하(1) -> 왼(2) -> 위(3))
        d_idx += 1
        if d_idx == 4:
            d_idx = 0

    # 종료조건 : num_list의 리스트를 벗어날 때 = idx = num_list_one의 가장 큰 값보다 커질 때
    if idx == max(num_list_one):
        break

for res in result:
    print(*res)