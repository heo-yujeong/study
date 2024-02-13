import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global result

    # 상하좌우를 탐색하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            # 미로 값이 0이면 1로 바꿔줌 => 다시 지나가지 않도록
            # 그 위치에서 재귀적으로 탐색
            if miro[nx][ny] == 0:
                miro[nx][ny] = 1
                dfs(nx, ny)
            # 미로 값이 3이면 = 목적지이면
            elif miro[nx][ny] == 3:
                # result를 1로 바꾸고 탐색 종료
                result = 1
                return

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N * N 행렬
    N = int(input())
    # 미로
    miro = [list(map(int, input())) for _ in range(N)]

    # 도착할 수 없다는 것을 초기값으로
    # 도착할 수 있을 때 1로 바꿔줌
    result = 0

    # 출발지 찾기 => 2인 곳을 찾음
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x, start_y = i, j

    # 시작위치부터 깊이우선탐색
    dfs(start_x, start_y)

    print(f'#{test_case} {result}')