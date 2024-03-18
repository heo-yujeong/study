import sys
sys.stdin = open('input.txt')

def backtrack(work, per):
    global max_per
    if work == N:
        max_per = max(max_per, per)
        return
    if max_per >= per:
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            backtrack(work+1, per*pij[work][i]*0.01)
            check[i] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    pij = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    max_per = 0
    backtrack(0, 1)

    print(f'#{test_case} {max_per*100:.6f}')