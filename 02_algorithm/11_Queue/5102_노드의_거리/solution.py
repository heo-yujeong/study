import sys
sys.stdin = open('input.txt')

def BFS(start, end):
    # 큐 생성
    queue = []
    queue.append(start)
    # 방문표시
    visited[start] = 1

    # 큐에 탐색할 노드가 남아있는 동안 반복
    while queue:
        start = queue.pop(0)
        # 이미 탐색한 적이 없고 연결되어 있으면 다음 탐색 노드로
        for next in range(1, V+1):
            if graph[start][next] == 1 and visited[next] == 0:
                # 방문표시를 하면서
                # 출발노드에서 몇개의 간선을 지나왔는지 같이 표시
                # 결과에는 -1 => 출발 노드를 1로 지정했기 때문
                visited[next] = visited[start] + 1
                queue.append(next)
                # 지금 방문할 예정인 노드가 도착노드와 같다면
                # 더이상 탐색하지 않고 종료
                if next == end:
                    return

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # V: 노드의 수, E: 간선의 수(무방향)
    V, E = map(int, input().split())
    # 그래프
    graph = [[0] * (V+1) for _ in range(V+1)]
    # 방문표시
    visited = [0] * (V+1)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 1

    # 출발노드, 도착노드
    S, G = map(int, input().split())

    # 출발점부터 도착점까지 탐색
    BFS(S, G)

    # visited[도착점] 값이 있으면 값-1, 값이 없으면 0
    print(f'#{test_case} {visited[G]-1 if visited[G] else 0}')