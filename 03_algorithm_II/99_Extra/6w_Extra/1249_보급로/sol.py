import sys
sys.stdin = open('input.txt')
from collections import deque

# 4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    # 시작점의 시간은 0으로
    time[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 더 빨리 도달할 수 있는 방법이 있다면
                if time[ny][nx] > time[y][x] + depth[y][x]:
                    # 더 빠른 시간으로 저장
                    time[ny][nx] = time[y][x] + depth[y][x]
                    # 다음 위치 탐색
                    queue.append((ny, nx))

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 지도의 크기
    N = int(input())
    # 지도(파손된 정도)
    depth = [list(map(int, list(input()))) for _ in range(N)]
    # 이동 시간 저장할 리스트 초기화
    # 최대 10만큼의 파손, 지도의 최대크기 100 => 최대크기로 초기화
    time = [[10*100] * N for _ in range(N)]

    bfs(0, 0)

    print(f'#{test_case} {time[N-1][N-1]}')