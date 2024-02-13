import sys
sys.stdin = open('input.txt')

def dfs(start):
    # 방문 표시
    visited[start] = 1
    # 이미 방문한 적이 없고, 연결되어 있으면 재귀적으로 방문표시
    for next in range(100):
        if not visited[next] and graph[start][next] == 1:
            dfs(next)


for _ in range(10):
    # T: 테스트 케이스 번호, N: 길의 총 개수
    T, N = map(int, input().split())

    # 순서쌍
    connect = list(map(int, input().split()))
    # 인접행렬 초기화
    graph = [[0] * 101 for _ in range(101)]
    # 방문여부 확인 행렬 초기화
    visited = [0] * 101
    # 순서쌍을 순회하면서 출발점, 도착점쌍을 인접행렬에 추가
    for n in range(N):
        start, end = connect.pop(0), connect.pop(0)
        graph[start][end] = 1

    # 깊이우선탐색(출발점은 0)
    dfs(0)

    # 0번에서 시작해서 갈 수 있는 모든 지점을 탐색했을 때
    # 99번 점을 지난 적이 있다 => visited[99] = 1
    # 지난적이 없다 => visited[99] = 0
    print(f'#{T} {visited[99]}')