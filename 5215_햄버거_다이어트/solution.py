import sys
sys.stdin = open('input.txt')

def select_food(cnt, cal_hap, score):
    global max_score
    if cal_hap > L:
        return
    if max_score < score:
        max_score = score
    if cnt == N:
        return
    select_food(cnt+1, cal_hap+TK[cnt][1], score+TK[cnt][0])
    select_food(cnt+1, cal_hap, score)


T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    TK = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    select_food(0, 0, 0)

    print(f'#{test_case} {max_score}')