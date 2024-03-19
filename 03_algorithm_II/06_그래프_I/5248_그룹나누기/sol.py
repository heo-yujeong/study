import sys
sys.stdin = open('input.txt')

def dfs(start):
    visit[start] = 1

    for next in choice[start]:
        if not visit[next]:
            dfs(next)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    apply = list(map(int, input().split()))
    choice = [[] for _ in range(N+1)]

    for i in range(M):
        ch1 = apply.pop(0)
        ch2 = apply.pop(0)
        choice[ch1].append(ch2)
        choice[ch2].append(ch1)

    visit = [0] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        if not visit[i]:
            dfs(i)
            cnt += 1

    print(f'#{test_case} {cnt}')