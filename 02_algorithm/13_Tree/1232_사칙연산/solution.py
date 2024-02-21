import sys
sys.stdin = open('input.txt')

def operator(node):
    # 연산자가 들어오면
    if oper_list[node] in '+-*/':
        # 왼쪽 자식노드 순회
        operator(tree[node][0])
        # 오른쪽 자식노드 순회
        operator(tree[node][1])
        # 연산자에 따라 계산한 값을 해당 노드에 넣어줌
        if oper_list[node] == '+':
            oper_list[node] = int(oper_list[tree[node][0]]) + int(oper_list[tree[node][1]])
        elif oper_list[node] == '-':
            oper_list[node] = int(oper_list[tree[node][0]]) - int(oper_list[tree[node][1]])
        elif oper_list[node] == '*':
            oper_list[node] = int(oper_list[tree[node][0]]) * int(oper_list[tree[node][1]])
        elif oper_list[node] == '/':
            oper_list[node] = int(oper_list[tree[node][0]]) // int(oper_list[tree[node][1]])

for test_case in range(1, 11):
    # 정점의 개수
    N = int(input())
    # 트리
    tree = [[0, 0] for _ in range(N+1)]
    # 연산자와 피연산자 저장
    oper_list = [0] * (N+1)

    for _ in range(N):
        # 노드 번호, (피)연산자, 자식노드
        node, oper, *child = input().split()
        oper_list[int(node)] = oper

        if len(child) == 2:
            tree[int(node)][0] = int(child[0])
            tree[int(node)][1] = int(child[1])
        elif len(child) == 1:
            tree[int(node)][0] = int(child[0])

    # 후위순회
    operator(1)
    print(f'#{test_case} {oper_list[1]}')