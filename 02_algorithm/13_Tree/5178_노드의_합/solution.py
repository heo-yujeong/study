import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 트리
    tree = [0] * (N+1)

    # 리프 노드와 값을 저장
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    # 자식 노드를 하나씩 부모 노드에 더해줌
    # 값이 N 부터 있기 때문에 역순으로
    for i in range(N, -1, -1):
        # 노드번호 i에 대해 부모 노드가 존재하면
        if i // 2 > 0:
            tree[i//2] += tree[i]

    print(f'#{test_case} {tree[L]}')