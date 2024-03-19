import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    E, start = map(int, input().split())
    edges = list(map(int, input().split()))
    connect = [[] * (max(edges)+1)]

    for i in range(E):
        from_, to_ = edges.pop(), edges.pop()
        connect[from_].append(to_)