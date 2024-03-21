import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    # 시작 위치는 거리 0으로 초기화
    dist[start] = 0

    while queue:
        start = queue.popleft()
        for next, w in graph[start]:
            # 더 작은 비용으로 갈 수 있다면
            if dist[next] > dist[start] + w:
                # 작은 값으로 바꿔줌
                dist[next] = dist[start] + w
                # 다음 위치 탐색
                queue.append(next)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 마지막 연결지점 번호, E: 도로의 개수
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    # 이동 거리 표시
    dist = [10*N] * (N+1)

    for _ in range(E):
        # s: 시작, e: 끝, w: 구간 거리
        s, e, w = map(int, input().split())
        # 방향이 있는 그래프
        graph[s].append([e, w])

    bfs(0)

    print(f'#{test_case} {dist[N]}')