import sys
sys.stdin = open('input.txt')

def backtrack(loc, oil, cnt, visit):
    global min_charge
    if loc + oil >= N:
        min_charge = min(cnt, min_charge)
        return

    if cnt > min_charge:
        return

    if oil <= 0:
        return

    if M[loc] == 0:
        backtrack(loc+1, oil-1, cnt, visit)
    else:
        backtrack(loc+1, M[loc], cnt+1, visit+[loc])
        backtrack(loc+1, oil-1, cnt, visit)


T = int(input())

for test_case in range(1, T+1):
    N, *M = map(int, input().split())

    min_charge = N

    backtrack(1, M[0], 0, [0])

    print(f'#{test_case} {min_charge}')