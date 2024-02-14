import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    queue = []
    queue.append((x, y))

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if miro[nx][ny] == 3:
                    return visited[x][y]
                elif miro[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x, start_y = i, j

    result = BFS(start_x, start_y)

    print(f'#{test_case} {result}')