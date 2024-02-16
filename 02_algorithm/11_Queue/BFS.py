def BFS(G, v): # 그래프G, 탐색 시작점v
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            # 방문해서 할 일 수행
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)