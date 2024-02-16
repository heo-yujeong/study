import sys
sys.stdin = open('input.txt')
# 출력 예시 1 2 3 4 5 7 6

def bfs(s, N): # 시작점, 노드수
    visited = [0] * (N+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in adjl[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    # 1번부터 각 자리까지 갈때 거리가 얼마인가?
    # -1 해주기(처음 출발점을 1로 했기 때문)
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(1, V)