import sys
sys.stdin = open('input.txt')

def dfs(i):
    visited[i] = 1
    print(i, end=' ')

    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

visited = [0] * (V+1)

dfs(1)