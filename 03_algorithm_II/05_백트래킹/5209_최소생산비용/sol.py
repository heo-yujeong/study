import sys
sys.stdin = open('input.txt')

def backtrack(line, cost):
    global min_cost
    if line == N:
        min_cost = min(min_cost, cost)
        return

    if cost > min_cost:
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            backtrack(line+1, cost+vij[line][i])
            check[i] = 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    vij = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    min_cost = 99 * N
    backtrack(0, 0)

    print(f'#{test_case} {min_cost}')