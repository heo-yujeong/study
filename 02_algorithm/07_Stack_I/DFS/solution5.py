# 인접 행렬 + 재귀

import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end=' ')
    for next in range(1, V+1):
        if visited[next] == 0 and adj[start][next] == 1:
            DFS(next)

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