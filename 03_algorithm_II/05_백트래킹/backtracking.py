# 중복된 순열
# 1 ~ 3까지 숫자 배열
# 111, 112, 113, ..., 333

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    # 기저조건
    if level == 3:
        print(*path)
        return

    # path[level] = 1
    # dfs(level + 1)
    #
    # path[level] = 2
    # dfs(level + 1)
    #
    # path[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level+1)

print('중복 순열')
dfs(0)

# 순열
# 1 ~ 3까지 숫자 배열
# 123, 132, 213, 231, 312, 321
path = [0] * 3

def dfs2(level):
    if level == 3:
        print(*path)
        return

    for i in range(len(arr)):
        if arr[i] not in path:
            path[level] = arr[i]
            dfs2(level+1)
            path[level] = 0

print('순열')
dfs2(0)