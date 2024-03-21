import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

def prim(start):
    pq = []
    MST = [0] * V
    sum_weight = 0 # 최소 비용
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        # 더 먼거리로 가는 방법이 큐에 저장이 되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        if MST[now]:
            continue
        MST[now] = 1
        sum_weight += weight

        for next in range(V):
            if not graph[now][next] or MST[next]:
                continue
            heappush(pq, (graph[now][next], next))

    print(f'최소 비용: {sum_weight}')

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

prim(0)