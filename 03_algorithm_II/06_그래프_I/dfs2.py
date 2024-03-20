# 인접리스트, 재귀
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * 5
path = []

def dfs(now):
    for next in graph[now]:
        if visited[next]:
            continue

        visited[next] = 1
        path.append(next)
        dfs(next)

visited[0] = 1
path.append(0)
dfs(0)
print(path)