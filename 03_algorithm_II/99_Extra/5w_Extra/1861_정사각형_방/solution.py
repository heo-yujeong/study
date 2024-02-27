import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start_x, start_y, cnt):
    queue = deque()
    queue.append((start_x, start_y, cnt))

    while queue:
        start_x, start_y, cnt = queue.popleft()
        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and rooms[start_x][start_y]+1 == rooms[nx][ny]:
                queue.append((nx, ny, cnt+1))
    return cnt


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            cnt = bfs(i, j, 1)
            if max_cnt < cnt:
                max_cnt = cnt
                stt_room = rooms[i][j]
            elif cnt == max_cnt and rooms[i][j] < stt_room:
                stt_room = rooms[i][j]

    print(f'#{test_case} {stt_room} {max_cnt}')