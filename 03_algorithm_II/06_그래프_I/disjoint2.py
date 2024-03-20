def make_set(x):
    parent = [i for i in range(x)]
    rank = [0] * x
    return parent, rank

def find_set(x):
    if parent[x] != x:
        return find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

parent, rank = make_set(7)
print(parent)
print(rank)
print()
union(1, 3)
print(parent)
print(rank)
print()
union(2, 3)
print(parent)
print(rank)
print()
union(5, 6)
print(parent)
print(rank)
print()
union(6, 3)
print(parent)
print(rank)