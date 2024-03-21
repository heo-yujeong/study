import sys
sys.stdin = open('input.txt')
from collections import deque

# 4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    # 시작 위치는 연료를 소비하지 않기 때문에 0으로
    dist[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 지금 위치와 다음 위치의 높이 차이
                # 작을 때는 추가 연료가 소요되지 않기 때문에 0으로 선택되도록
                diff = max(height[ny][nx] - height[y][x], 0)
                # 다음 위치갈때 드는 연료가 현재 위치에서 이동할 때 연료보다 많다면
                if dist[ny][nx] > dist[y][x] + diff + 1:
                    # 작은 값으로 대체!
                    dist[ny][nx] = dist[y][x] + diff + 1
                    # 다음 위치 탐색
                    queue.append((ny, nx))

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 지역 개수
    N = int(input())
    # 지역의 높이
    height = [list(map(int, input().split())) for _ in range(N)]

    # 해당 위치까지 이동하는 데 드는 최소 연비 소비량 체크
    # 최대 1000까지의 높이, 추가되는 연료의 최대 1000 => 2001로 초기화
    dist = [[2001] * N for _ in range(N)]

    bfs(0, 0)

    print(f'#{test_case} {dist[N-1][N-1]}')