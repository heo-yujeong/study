# 1~6까지 노드 존재
# 1. make_set
def make_set(n):
    return [i for i in range(n)]

parents = make_set(7)
# 2. fine_set
# 부모 노드를 보고, 부모 노드도 연결이 되어있다면 반복
# 자기 자신의 대표 데이터를 찾을 때까지
def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)
union(5, 6)
print(find_set(6))
print(parents)