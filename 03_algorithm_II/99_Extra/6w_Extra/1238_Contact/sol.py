import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()
        for next in connect[start]:
            if not visit[next]:
                visit[next] = visit[start] + 1
                queue.append(next)

for test_case in range(1, 11):
    E, start = map(int, input().split())
    edges = list(map(int, input().split()))
    connect = [[] for _ in range(max(edges)+1)]
    visit = [0] * (max(edges) + 1)

    for _ in range(E//2):
        to_, from_ = edges.pop(), edges.pop()
        connect[from_].append(to_)

    bfs(start)

    max_val = max(visit)
    max_lst = []
    for i in range(len(visit)):
        if visit[i] == max_val:
            max_lst.append(i)

    print(f'#{test_case} {max(max_lst)}')