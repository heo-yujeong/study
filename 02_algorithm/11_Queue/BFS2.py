def BFS(G, v, n): # 그래프G, 탐색 시작점v
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        # 방문해서 할 일 수행
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1