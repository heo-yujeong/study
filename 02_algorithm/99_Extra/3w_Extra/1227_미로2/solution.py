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

    while queue:
        x, y = queue.popleft()
        # 4방향 확인
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < 100 and 0 <= ny < 100:
                # 다음 위치가 도착점(3)이면
                if miro[nx][ny] == 3:
                    # 도착할 수 있음을 알려주고 종료
                    result = 1
                    return
                # 다음 위치가 길이면
                elif miro[nx][ny] == 0:
                    # 다음 이동을 할 수 있도록 큐에 삽입
                    queue.append((nx, ny))
                    # 다시 해당 위치를 탐색하지 않도록 miro의 값을 1로 변환
                    # visited 생성 X
                    miro[nx][ny] = 1

for _ in range(10):
    # 테스트 케이스
    test_case = int(input())
    # 100 * 100 미로
    miro = [list(map(int, input())) for _ in range(100)]
    # 도착할 수 없음으로 초기화
    result = 0

    # 출발점 탐색
    for i in range(100):
        for j in range(100):
            if miro[i][j] == 2:
                start_x, start_y = i, j

    # 출발점 ~ 도착점 도달 가능한지 확인
    BFS(start_x, start_y)

    print(f'#{test_case} {result}')