import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    # 큐 생성
    queue = []
    queue.append((x, y))

    # 다음 탐색할 위치가 있는 동안 반복
    while queue:
        # 현재 위치
        x, y = queue.pop(0)
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 있는 길이고 간 적이 없는 길일때
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 다음 위치가 도착점(3)일때
                if miro[nx][ny] == 3:
                    # 이동 거리 = 이전위치까지의 visited에 저장된 값 return
                    return visited[x][y]
                # 다음 위치가 길(0)일때(이동할 수 있는 위치일때)
                elif miro[nx][ny] == 0:
                    # visited의 값을 이전 값 + 1로 변경 후 스택에 위치 삽입
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return 0

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N * N 크기
    N = int(input())
    # 미로
    # 1: 벽, 0: 통로, 2: 출발, 3: 도착
    miro = [list(map(int, input())) for _ in range(N)]
    # 방문표시
    visited = [[0] * N for _ in range(N)]

    # 출발지점 탐색
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x, start_y = i, j

    result = BFS(start_x, start_y)

    print(f'#{test_case} {result}')