import sys
sys.stdin = open('input.txt')

def dfs(i, V): # 시작, 끝
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1
    print(i, end=' ')

    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                print(i, end=' ')
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
# adjl[i] 행 : i행에 인접인 정점 번호
adjl = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 그래프이기 때문에 추가

dfs(1, V)