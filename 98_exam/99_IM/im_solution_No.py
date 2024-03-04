import sys
sys.stdin = open('input.txt')

def calc(block_lst):
    weight = 0
    for i in range(len(block_lst)):
        weight += ((i+1) * block_lst[i])
    return weight

def select(cnt, block_m1, len_m1, block_m2, len_m2):
    global min_wei
    if cnt == N:
        if len_m1 == M1:
            hap = calc(block_m1) + calc(block_m2)
            if min_wei > hap:
                min_wei = hap
        return

    if len_m1 > M1 or len_m2 > M2:
        return

    select(cnt + 1, block_m1 + [block[cnt]], len_m1+1, block_m2, len_m2)
    select(cnt + 1, block_m1, len_m1, block_m2 + [block[cnt]], len_m2+1)


T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort(reverse=True)
    min_wei = 1000 * N * N

    select(0, [], 0, [], 0)

    print(f'#{tc} {min_wei}')