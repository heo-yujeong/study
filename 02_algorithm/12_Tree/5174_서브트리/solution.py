import sys
sys.stdin = open('input.txt')

# 전위 순회하는 함수
def preorder(node):
    # 순회를 하는 동안 cnt에 1씩 더해줌 => 노드가 존재한다!
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # E: 간선의 개수, N: 서브트리 조사할 루트 노드 번호
    E, N = map(int, input().split())
    # 부모 자식 노드 번호쌍
    arr = list(map(int, input().split()))
    # 노드의 개수
    V = max(arr)

    # 트리 생성
    tree = [[0, 0] for _ in range(V + 1)]
    for idx in range(E):
        if tree[arr[idx * 2]][0] == 0:
            tree[arr[idx * 2]][0] = arr[idx * 2 + 1]
        else:
            tree[arr[idx * 2]][1] = arr[idx * 2 + 1]

    # 서브트리에 속한 노드의 개수 count
    cnt = 0
    # 전위 순회 실시
    preorder(N)
    print(f'#{test_case} {cnt}')