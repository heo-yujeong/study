import sys
sys.stdin = open('input.txt')
from collections import deque

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    global result
    # 큐 생성
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        # 4방향을 확인하면서
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 미로를 벗어나지 않으면서 아직 가지 않은 곳이면
            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == 0:
                # 다음 위치가 도착점(3)이라면
                if miro[nx][ny] == 3:
                    # 도착할 수 있음을 알려주고 종료
                    result = 1
                    return
                # 다음 위치가 갈 수 있는 길이라면
                elif miro[nx][ny] == 0:
                    # 방문표시
                    visited[nx][ny] = 1
                    # 다음 위치를 찾기 위해 큐에 위치 삽입
                    queue.append((nx, ny))

for _ in range(10):
    # 테스트 케이스
    test_case = int(input())
    # 16*16 행렬
    # 1: 벽, 0: 길, 2: 출발점, 3: 도착점
    miro = [list(map(int, input())) for _ in range(16)]
    # 방문 여부 체크
    visited = [[0] * 16 for _ in range(16)]

    # 도착할 수 없다고 가정
    result = 0

    # 출발점 탐색
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                start_x, start_y = i, j

    # 출발점 ~ 도착점 도달 가능한지 확인
    BFS(start_x, start_y)

    print(f'#{test_case} {result}')