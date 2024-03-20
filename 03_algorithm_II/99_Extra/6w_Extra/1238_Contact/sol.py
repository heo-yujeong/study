import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()
        for next in connect[start]:
            if not visit[next]:
                # 늦게 연락을 받을 수록 visit의 숫자 높아짐
                visit[next] = visit[start] + 1
                queue.append(next)


# 10개의 테스트 케이스
for test_case in range(1, 11):
    # E: 입력 데이터 길이, start: 시작점
    E, start = map(int, input().split())
    # 간선 정보
    edges = list(map(int, input().split()))
    # 간선 정보를 나타낼 인접 리스트
    connect = [[] for _ in range(max(edges)+1)]
    # 방문 체크 배열
    visit = [0] * (max(edges) + 1)

    for _ in range(E//2):
        to_, from_ = edges.pop(), edges.pop()
        # 연락하는 사람의 인덱스에 연락 받을 수 있는 번호 추가
        # ex) 100 17 => 100번이 17번에게 연락 가능
        # => connect[100] 에 17추가
        connect[from_].append(to_)

    # print(connect)
    bfs(start)

    # visit에서 가장 큰 값이 있는 곳들의 위치에서 가장 큰 값 출력
    max_val = max(visit)
    max_lst = []
    for i in range(len(visit)):
        if visit[i] == max_val:
            max_lst.append(i)

    print(f'#{test_case} {max(max_lst)}')