import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

def prime(start):
    global min_hap
    pq = []
    heappush(pq, (0, start))

    while pq:
        w, now = heappop(pq)
        # 아직 해당 노드를 방문하지 않았을 때만 조사
        if not visit[now]:
            # 방문 표시
            visit[now] = 1
            # 가중치 더해줌
            min_hap += w
            for nw, next in graph[now]:
                # 아직 다음 위치를 방문하지 않았다면
                if not visit[next]:
                    # 가중치와 노드번호를 pq에 등록
                    heappush(pq, (nw, next))

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # V: 노드 끝번호, E: 간선 개수
    V, E = map(int, input().split())
    # 그래프 초기화
    graph = [[] for _ in range(V+1)]
    # 방문 표시
    visit = [0] * (V+1)
    for _ in range(E):
        # n1~2: 노드 번호, w: 간선의 가중치
        n1, n2, w = map(int, input().split())
        graph[n1].append([w, n2])
        graph[n2].append([w, n1])

    # 최소신장트리 구성하는 가중치 합계
    min_hap = 0
    prime(0)
    print(f'#{test_case} {min_hap}')