import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(num):
    queue = deque()
    queue.append(num)

    while queue:
        num = queue.popleft()
        for _ in range(4):
            if 0 < num+1 < 1000001 and not visit[num+1]:
                visit[num+1] = visit[num] + 1
                queue.append(num+1)
                if num+1 == M:
                    return
            if 0 < num-1 < 1000001 and not visit[num-1]:
                visit[num-1] = visit[num] + 1
                queue.append(num-1)
                if num-1 == M:
                    return
            if 0 < num*2 < 1000001 and not visit[num*2]:
                visit[num*2] = visit[num] + 1
                queue.append(num*2)
                if num*2 == M:
                    return
            if 0 < num-10 < 1000001 and not visit[num-10]:
                visit[num-10] = visit[num] + 1
                queue.append(num-10)
                if num-10 == M:
                    return

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    visit = [0] * 1000001

    bfs(N)

    print(f'#{test_case} {visit[M]}')