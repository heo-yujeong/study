# 인접행렬, 재귀
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]
visited = [0] * 5
path = []

def dfs(now):
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue

        visited[next] = 1
        path.append(next)
        dfs(next)

visited[0] = 1
path.append(0)
dfs(0)
print(path)