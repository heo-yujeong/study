import sys
sys.stdin = open('input.txt')

def select_food(cnt, cal_hap, score):
    global max_score
    if cnt <= N:
        if cal_hap <= L:
            if max_score < score:
                max_score = score
    if cal_hap > L:
        return
    else:
        for i in range(N):
            if i not in select:
                select.add(i)
                select_food(cnt+1, cal_hap+TK[i][1], score+TK[i][0])
                select.remove(i)

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    TK = [list(map(int, input().split())) for _ in range(N)]
    select = set()
    max_score = 0
    select_food(0, 0, 0)

    print(f'#{test_case} {max_score}')