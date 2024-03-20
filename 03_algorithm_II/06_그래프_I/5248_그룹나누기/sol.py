import sys
sys.stdin = open('input.txt')

def dfs(start):
    visit[start] = 1

    for next in choice[start]:
        if not visit[next]:
            dfs(next)

# 테스트 케이스
T = int(input())

for test_case in range(1, T+1):
    # N: 사람 수, M: 신청서 수
    N, M = map(int, input().split())
    # 신청서
    apply = list(map(int, input().split()))
    # 신청서를 토대로 연결 리스트 생성(무방향)
    choice = [[] for _ in range(N+1)]

    for i in range(M):
        ch1 = apply.pop(0)
        ch2 = apply.pop(0)
        choice[ch1].append(ch2)
        choice[ch2].append(ch1)

    # 이미 방문한 곳인치 체크
    visit = [0] * (N+1)
    # 조 갯수
    cnt = 0

    for i in range(1, N+1):
        if not visit[i]:
            dfs(i)
            cnt += 1

    print(f'#{test_case} {cnt}')