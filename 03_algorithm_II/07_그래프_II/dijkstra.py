import sys
sys.stdin = open('input2.txt')
from heapq import heappush, heappop

INF = int(1e9)
V, E = map(int, input().split())
start = 0 # 시작 노드 번호

graph = [[] for _ in range(V)]
# 누적 거리
distance = [INF] * V
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        # 이미 처리된 노드는 pass
        # = now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_dist = next[0]
            next_node = next[1]

            new_dist = dist + next_dist # 누적 거리 계산
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node))

dijkstra(start)
print(distance)