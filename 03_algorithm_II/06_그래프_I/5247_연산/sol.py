import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(num):
    queue = deque()
    queue.append(num)

    while queue:
        num = queue.popleft()
        # +1 을 했을 때 값이 만들어질 경우
        # 단, 이전에 만든 적이 없을 때
        # => 이미 만든 적이 있다면 더 적은 횟수로 만들었을테니!
        if 0 < num+1 < 1000001 and not visit[num+1]:
            visit[num+1] = visit[num] + 1
            queue.append(num+1)
            if num+1 == M:
                return
        # -1 을 했을 때 값이 만들어질 경우
        if 0 < num-1 < 1000001 and not visit[num-1]:
            visit[num-1] = visit[num] + 1
            queue.append(num-1)
            if num-1 == M:
                return
        # *2 을 했을 때 값이 만들어질 경우
        if 0 < num*2 < 1000001 and not visit[num*2]:
            visit[num*2] = visit[num] + 1
            queue.append(num*2)
            if num*2 == M:
                return
        # -10 을 했을 때 값이 만들어질 경우
        if 0 < num-10 < 1000001 and not visit[num-10]:
            visit[num-10] = visit[num] + 1
            queue.append(num-10)
            if num-10 == M:
                return

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 처음 자연수, M: 목표 자연수
    N, M = map(int, input().split())
    # 중간에 만들어지는 자연수 체크
    visit = [0] * 1000001

    bfs(N)

    print(f'#{test_case} {visit[M]}')