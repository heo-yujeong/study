import sys
sys.stdin = open('input.txt')

def calc(comb):
    global max_rst, min_rst
    result = num_lst[0]
    for i in range(1, N):
        if comb[i-1] == '+':
            result += num_lst[i]
        elif comb[i-1] == '-':
            result -= num_lst[i]
        elif comb[i-1] == '*':
            result *= num_lst[i]
        else:
            result /= num_lst[i]
            result = int(result)

    if min_rst > result:
        min_rst = result
    if max_rst < result:
        max_rst = result

def oper_comb(cnt, max_cnt, comb):
    if cnt == max_cnt:
        calc(comb)
        return
    for i in range(4):
        if oper_cnt[i] > 0:
            oper_cnt[i] -= 1
            oper_comb(cnt+1, max_cnt, comb+[oper[i]])
            oper_cnt[i] += 1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    oper_cnt = list(map(int, input().split()))
    oper = ['+', '-', '*', '/']
    num_lst = list(map(int, input().split()))

    max_rst = -100000000
    min_rst = 100000000

    oper_comb(0, sum(oper_cnt), [])

    print(f'#{test_case} {max_rst-min_rst}')