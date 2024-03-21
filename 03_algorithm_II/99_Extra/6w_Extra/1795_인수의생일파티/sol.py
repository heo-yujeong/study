import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start, graph):
    # 시작 위치에서 각 위치로 가는데 걸리는 시간 초기화
    # 최대 거리 100, 집 개수 N => 100*N으로 초기화
    time = [100*N] * (N+1)
    queue = deque()
    queue.append(start)
    # 시작 위치에서는 시간이 소요되지 않음
    time[start] = 0

    while queue:
        start = queue.popleft()
        for next, w in graph[start]:
            # 더 적은 시간으로 갈 수 있는 방법이 있다면
            if time[next] > time[start] + w:
                # 적은 시간으로 값 저장하고
                time[next] = time[start] + w
                # 다음 위치 탐색
                queue.append(next)
    return time

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 집 개수, M: 도로 개수, X: 목적지(출발지)
    N, M, X = map(int, input().split())
    # 목적지 - 각 집까지의 거리
    # 갈때, 올때 시간이 다르기 때문에 2개 따로
    go = [[] for _ in range(N+1)]
    come = [[] for _ in range(N+1)]

    for _ in range(M):
        # x: 출발, y: 도착, c: 시간
        x, y, c = map(int, input().split())
        go[x].append([y, c])
        come[y].append([x, c])

    # 가는 시간
    go_time = bfs(X, go)
    # 돌아오는 시간
    come_time = bfs(X, come)

    # 최대로 걸리는 시간
    max_time = 0
    for i in range(1, N+1):
        # 가는 시간+오는 시간이 가장 큰 값으로
        max_time = max(max_time, go_time[i]+come_time[i])

    print(f'#{test_case} {max_time}')