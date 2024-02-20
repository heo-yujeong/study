import sys
sys.stdin = open('input.txt')

'''
[이진 트리 노드 번호의 성질]
- 노드 번호가 i인 노드의 부모 노드 번호 : i // 2
- 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2 * i
- 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2 * i + 1
- 레벨 n의 노드 번호 시작 번호 : 2 ** n
'''

# 중위 순회를 하는 함수
def inorder(node):
    global num
    if node and node <= N:
        inorder(2*node)
        # num를 tree[node]에 저장하고 +1
        tree[node] = num
        num += 1
        inorder(2*node+1)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # 노드의 개수
    N = int(input())
    # 트리에 저장할 자연수(1~N)
    num = 1
    # 완전 이진 트리
    tree = [0] * (N+1)

    # 중위 순회
    inorder(1)
    # 루트에 저장된 값, N//2번 노드에 저장된 값
    print(f'#{test_case} {tree[1]} {tree[N//2]}')
