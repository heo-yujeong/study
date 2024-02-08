# 인접 행렬

import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = [start]
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')
            # 0번 노드를 제외한 모든 노트번호가 now버 위치에서 이동 가능한지
            for next in range(V, 0, -1):
                if visited[next] == 0 and adj[now][next] == 1:
                    stack.append(next)


# V : voltex (정점, 노드)
# E : Edge (간선)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V+1)

# 인접행렬
adj = [[0] * (V+1) for _ in range(V+1)]
for idx in range(E):
    adj[arr[idx*2]][arr[idx*2+1]] = 1
    adj[arr[idx*2+1]][arr[idx*2]] = 1

DFS(1)