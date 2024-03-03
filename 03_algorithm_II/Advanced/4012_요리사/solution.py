import sys
sys.stdin = open('input.txt')

def choice_calc(cnt, alst, blst):
    global min_dif
    if cnt == N:
        if len(alst) == N//2:
            asng = bsng = 0
            for i in range(N//2):
                for j in range(N//2):
                    asng += Sij[alst[i]][alst[j]]
                    bsng += Sij[blst[i]][blst[j]]
            if min_dif > abs(asng-bsng):
                min_dif = abs(asng-bsng)
        return

    choice_calc(cnt+1, alst+[cnt], blst)
    choice_calc(cnt+1, alst, blst+[cnt])


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Sij = [list(map(int, input().split())) for _ in range(N)]
    select = [0] * N
    min_dif = 20000 * N * N

    choice_calc(0, [], [])

    print(f'#{test_case} {min_dif}')