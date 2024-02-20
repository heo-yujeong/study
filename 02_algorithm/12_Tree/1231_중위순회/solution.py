import sys
sys.stdin = open('input.txt')

# 중위 순회를 하는 함수
def inorder(node):
    # 현재 노드가 있을 때
    if node:
        # 왼쪽 자식 노드 순회
        inorder(tree[node][0])
        # 현재 노드 할일 수행
        # 할일 = 알파벳을 담은 리스트의 본인의 인덱스에 담긴 알파벳 출력
        print(txt_list[node], end='')
        # 오른쪽 자식 노드 순회
        inorder(tree[node][1])


for test_case in range(1, 11):
    # 정점의 총 수
    N = int(input())
    # 알파벳을 담을 리스트
    txt_list = [0] * (N+1)
    # 트리 생성
    tree = [[0, 0] for _ in range(N+1)]

    # 모든 정점의 정보가 주어지는 동안
    for _ in range(N):
        # 정점의 정보 받음
        # [정점 번호, 알파벳, 왼쪽 자식노드, 오른쪽 자식노드]
        info = input().split()
        # 정점 번호에 해당하는 알파벳을 txt_list에 담음
        txt_list[int(info[0])] = info[1]
        # 왼쪽 자식노드가 있을 때 정보 저장
        if len(info) > 2:
            tree[int(info[0])][0] = int(info[2])
        # 오른쪽 자식노드가 있을 떄 정보 저장
        if len(info) > 3:
            tree[int(info[0])][1] = int(info[3])

    print(f'#{test_case}', end=' ')
    # 중위 순회 실시
    inorder(1)
    print()