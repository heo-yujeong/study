import sys
sys.stdin = open('input.txt')

def backtrack(loc, cnt):
    global min_charge
    if loc == N-1:
        min_charge = min(cnt, min_charge)
        return

    if cnt >= min_charge:
        return

    for i in range(1, M[loc]+1):
        backtrack(loc+i, cnt+1)


T = int(input())

for test_case in range(1, T+1):
    N, *M = map(int, input().split())

    min_charge = N
    backtrack(0, -1)

    print(f'#{test_case} {min_charge}')