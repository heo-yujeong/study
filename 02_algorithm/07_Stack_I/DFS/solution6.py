# 인접 리스트 + 재귀

import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end=' ')
    for next in adj[start]:
        if visited[next] == 0:
            DFS(next)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adj = [[] for _ in range(V+1)]
for idx in range(0, E*2, 2):
    from_node, to_node = arr[idx], arr[idx+1]
    adj[from_node].append(to_node)
    adj[to_node].append(from_node)

visited = [0] * (V+1)
DFS(1)