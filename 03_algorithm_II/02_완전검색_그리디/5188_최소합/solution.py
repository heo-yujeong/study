import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def search(x, y):
    stack = [[x, y, data[x][y]]]

    while stack:
        x, y, cnt = stack.pop()
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N:
                if visited[nx][ny] > cnt+data[nx][ny]:
                    visited[nx][ny] = cnt+data[nx][ny]
                    stack.append([nx, ny, cnt+data[nx][ny]])

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[10*N*N] * N for _ in range(N)]
    search(0, 0)

    print(f'#{test_case} {visited[N-1][N-1]}')