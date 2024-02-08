# 인접 리스트

import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = [start]
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')
            for next in adj[now]:
                if visited[next] == 0:
                    stack.append(next)


# V : voltex (정점, 노드)
# E : Edge (간선)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
# 노드 = 인덱스로 하기 위해 노드 수 + 1
# 인덱스는 0부터 시작이니까!
adj = [[] for _ in range(V+1)]
for idx in range(0, E*2, 2):
    from_node, to_node = arr[idx], arr[idx+1]
    adj[from_node].append(to_node)
    adj[to_node].append(from_node)

visited = [0] * (V+1)
DFS(1)