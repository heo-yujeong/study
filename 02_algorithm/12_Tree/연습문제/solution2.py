import sys
sys.stdin = open('input.txt')

def solution(k):
    print(k, end=' ')

# 전위순회
def preorder(now):# 조사 시작 노드번호부터 조사 시작
    # 현재 노드 번호에 대해 할일 수행
    if now:
        solution(now)
        # 왼쪽 자식 순회
        preorder(tree[now][0])
        # 오른쪽 자식 순회
        preorder(tree[now][1])

# 중위순회
def inorder(now):
    if now:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

# 후위순회
def postorder(now):
    if now:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)


# 노드 개수
V = int(input())
# 간선 정보
edge = list(map(int, input().split()))
# 간선 정보 길이
E = len(edge)
'''
# 인접 리스트
adj = [[] for _ in range(V+1)]
for idx in range(E//2):
    adj[edge[idx*2]].append(edge[idx*2+1])
print(adj)
'''
# 처음부터 이진트리의 형태로
tree = [[0, 0] for _ in range(V+1)]
for idx in range(E//2):
    # 왼쪽 자식 정보가 아직 없다면
    if tree[edge[idx*2]][0] == 0:
        tree[edge[idx*2]][0] = edge[idx*2+1]
    # 왼쪽 자식 정보가 이미 있다면
    else:
        # 오른쪽에 삽입
        tree[edge[idx*2]][1] = edge[idx*2+1]

print('전위순회')
preorder(1)
print()
print('중위순회')
inorder(1)
print()
print('후위순회')
postorder(1)