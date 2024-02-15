import sys
sys.stdin = open('input.txt')

for test_case in range(1, 2):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        s, e = arr.pop(0), arr.pop(0)
        graph[s][e] = 1
