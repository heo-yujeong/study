import sys
sys.stdin = open('input.txt')

def calc_func(num, target, cnt):
    global min_cnt
    if num == target:
        min_cnt = min(min_cnt, cnt)
        return

    if cnt >= min_cnt:
        return

    calc_func(num*2, target, cnt+1)
    calc_func(num+1, target, cnt+1)
    calc_func(num-1, target, cnt+1)
    calc_func(num-10, target, cnt+1)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    min_cnt = abs(M-N+1)
    calc_func(N, M, 0)

    print(f'#{test_case} {min_cnt}')