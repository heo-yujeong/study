import sys
sys.stdin = open('input.txt')

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
edges.sort(key=lambda x:x[2]) # 가중치 기준으로 정렬

parents = [i for i in range(V)]
cnt = 0
sum_weight = 0

for s, e, w in edges:
    # 싸이클 O = 이미 같은 집합에 속해 있다면 => pass
    if find_set(s) == find_set(e):
        continue
    # 싸이클 X
    cnt += 1
    union(s, e)
    sum_weight += w

    # MST 완성 = 간선의 개수 == V-1
    if cnt == V-1:
        break

print(f'최소 비용: {sum_weight}')