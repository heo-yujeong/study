# 인접 리스트
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * 5

def bfs(start):

    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            queue.append(next)

bfs(0)