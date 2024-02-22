# 아래부터 탐색(재귀함수)

import sys
sys.stdin = open('input.txt')

# 좌 우 상 => 위로 올라가는 경우의 우선순위가 가장 낮기 때문
dx = [0, 0, -1]
dy = [-1, 1, 0]

def search(x, y):
    if x == 0: # 제일 위에 도착했다면
        return y

    for i in range(3) : # 3방향 조사
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = 1
            return search(nx, ny)


for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[0] * 100 for _ in range(100)]
    result = 0
    # 출발 지점
    for i in range(100):
        if arr[99][i] == 2:
            result = search(99, i)
            print(i)
    print(f'#{test_case} {result}')